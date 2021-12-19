import json
from flask import Flask, render_template, jsonify, request, make_response
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from os.path import join, dirname, realpath

app = Flask(__name__)
tokenizer = AutoTokenizer.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')


@app.route('/amazon/', methods=["POST"])
def my_view_func():
    if request.method == 'POST':
      url = request.form.get('url')
      if url is None or url == "":
            resp = make_response("Please upload CSV file", 400)
            return resp
      else:
        my_dict = {'response': '200', "Positive_Review": [],
            "Negative_Review": [], "Neutral_Review": []}
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/90.0.4430.212 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
              review = item.get_text()
              rating = sentiment_score(review)
              type = "positive" if rating > 3 else (
                  "negative" if rating < 3 else "neutral")
              dict = {"review": review, "rating": rating, "type": type}
              if type == "positive":
                    my_dict["Positive_Review"].append(dict)
              elif type == "negative":
                    my_dict["Negative_Review"].append(dict)
              else:
                    my_dict["Neutral_Review"].append(dict)
        return jsonify(my_dict)


def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt', truncation=True)
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


@app.route("/analytics", methods=['POST'])
def analytics():
    if request.method == 'POST':
        if 'file' not in request.files:
            resp = make_response("Please upload CSV file", 400)
            return resp
        else:
            my_dict = {'response': '200', "Positive_Review": [],
                "Negative_Review": [], "Neutral_Review": []}
            file = request.files['file']
            data = pd.read_csv(file,sep=",", header=None,nrows=100)[9]
            try:
                for row in data:
                      review = row
                      rating = sentiment_score(review)
                      type = "positive" if rating > 3 else (
                            "negative" if rating < 3 else "neutral")
                      dict = {"review": review,
                            "rating": rating, "type": type}
                      if type == "positive":
                              my_dict["Positive_Review"].append(dict)
                      elif type == "negative":
                              my_dict["Negative_Review"].append(dict)
                      else:
                              my_dict["Neutral_Review"].append(dict)

                return jsonify(my_dict)
            except Exception as ex:
                print(ex)
            


@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
