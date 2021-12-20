# Product Review Sentiment Analysis using Bert

<img src="https://github.com/yassinebenabbes/Api_Sentiment_Analysis_Product_Reviews/blob/master/img/55259main.png" align="right"
     alt="Sentiment Analysis logo" width="320" height="200">

One of the key areas where NLP is mainly used is sentiment analysis. Understanding customer behavior and demand for the company's products and services is critical to the organization. Generally speaking, customer feedback on the product can be divided into positive, negative and neutral. Explaining customer feedback through product reviews helps companies assess customer satisfaction with their products/services.
If polarity accuracy is important to your business, you can consider expanding the polarity category to include:



* **Very Negative**
* **Negative**
* **Neutral**
* **Positive**
* **Very Positive**


**BERT(bi-directional Encoder Representation of Transformers)** is a machine learning technique developed by Google based on the Transformers mechanism. In our sentiment analysis application, our model is trained on a pre-trained BERT model. BERT models have replaced the conventional RNN based LSTM networks. They can easily understand the context of a word in a sentence based on previous words in the sentences due to its bi-directional approach.

<p align="center">
<img src="https://www.codemotion.com/magazine/wp-content/uploads/2020/05/bert-google-1200x675.png"
  alt="bERT"
  width="450" height="250">
</p>

## How to use 

1. Install and Import Dependencies
<p align="center">
<img src="https://github.com/yassinebenabbes/Api_Sentiment_Analysis_Product_Reviews/blob/master/img/carbon.png"
  alt="bERT"
  width="650" height="250">
</p>
2. Instantiate Model
<p align="center">
<img src="https://github.com/yassinebenabbes/Api_Sentiment_Analysis_Product_Reviews/blob/master/img/carbon%20(1).png"
  alt="bERT"
  width="650" height="250">
</p>

3. Encode and Calculate Sentiment
<p align="center">
<img src="https://github.com/yassinebenabbes/Api_Sentiment_Analysis_Product_Reviews/blob/master/img/carbon%20(2).png"
  alt="bERT"
  width="650" height="250">
</p>

4. Run flask application using flask run command
<p align="center">
<img src="https://github.com/yassinebenabbes/Api_Sentiment_Analysis_Product_Reviews/blob/master/img/carbon%20(3).png"
  alt="bERT"
  width="650" height="250">
</p>

## Usage

### The api provide two route :


<details><summary><b> /Amazon </b></summary>

1. Post Method:
          - **Query Params** :
                    **Url** = "Amazon Product url "

    ``` sh 
     http://127.0.0.1:5000/amazon?url= "url"
    ```

2. Example And Result :
     
     2.1 - Example
     ``` sh 
     http://127.0.0.1:5000/amazon?url= "https://www.amazon.com/Amazfit-Android-Fitness-Display-Tracking/dp/B09H5TWZQT/ref=sr_1_1_sspa?keywords=fitness+GPS&pf_rd_i=21439846011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=67c6cf47-c067-447f-a799-b2cb009a7a6e&pf_rd_r=9QQMNCA3BQF4XZCH232H&pf_rd_s=merchandised-search-8&pf_rd_t=101&qid=1640000071&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQVNEUzY5TEZUT0ROJmVuY3J5cHRlZElkPUEwOTExMTAzM0ZIMVY4QzZDSTNNTCZlbmNyeXB0ZWRBZElkPUEwMTE2NzE5Mk81TFdEVUJDOVhITiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    ```
     2.2 - Result
     
    ``` sh
     {
    "Negative_Review": [
        {
            "rating": 1,
            "review": "\n\n  If you're into fitness please don't get this. I tested it vs known good polar chest strap and Garmin venu and those worked well where the Amafit heartrate couldn't keep up it would make my heartrate randomly dip to 50bpm while my other bands said 140. I got 10 hours of sleep one night and it gave me 6 hours. This is off 3 days of testing and heartrate and sleep tracking were way off.\n\n",
            "type": "negative"
        }
    ],
    "Neutral_Review": [
        {
            "rating": 3,
            "review": "\n\n  Me gusto la forma del producto y las imágenes. También las opciones de medir el stress y el oxigeno. Me ha sido bastante preciso en cuanto al sueño . Me gusta mucho la rotación que tiene el marcador horario, permite ver rápidamente las opciones. Creo que sobrevenden la automatización de los ejercicios. No es automático de pasar de un ejercicio a otro. Tienes que hacer al cambio manual. Recoge bien las caminatas pero si pasas a otro ejercicio por algunos minutos (por ejemplo elíptica) tienes que detenerte y cambiar a elíptica y luego si continuas en caminata tienes que detener elíptica y anotar caminata.  De alguna forma pierdes algo del impulso que llevas. Me preocupa si viajo a Europa con el voltaje 220 porque no podré cambiar de los 110 V de los EUA y en este sentido el reloj es inútil. En ninguna parte menciona como se puede lograr la convertibilidad de 110 V a 220 V.  Para poder emparejar con la app Zepp el proceso fue largo y complicado.  Es muy difícil comunicarse con la casa Amazfit para preguntas y si lo logras no responden.\n\n",
            "type": "neutral"
        }
    ],
    "Positive_Review": [
        {
            "rating": 5,
            "review": "\n\n  My daughter showed me an Amazfit GTR 3 Pro she recently purchased and how easy it was to use, and it looked gorgeous on her.  I needed something that looked stylish while monitoring my heart rate, oxygen level, breathing rate, etc. So we searched upon this brand to see what other watches it has to offer.  And I laid my eyes on this rosa color watch, the screen size is just right, not too big for the wrist, yet I was able to see all the text on the big display.  My daughter helped me set this up in just a few minutes.  And I’ve been wearing it since, received so many compliments from others.  Now I have a piece of mind to track how active I am, and if I were sitting too long, it’d remind me to get up and walk a little.  I also love how it monitors sleep patterns; and suggests ways to reduce stress, such as breathing exercises, to help you improve sleep quality.  The biggest plus is, I had not needed to recharge it since I got the watch (it was at 89% battery when I got it last week); now, almost a week has gone by, it is still running smoothly (you don’t have to charge it daily like the other smartwatches).\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  I purchased the Amazfit GTS 3 to replace my ZTE quartz that died about a year ago. I noticed the GTS 3 is a new model so I decided to try it out.  It's been about a week since I received it and the battery is still going strong.  I've been waiting for a smart watch that does not require charging every day and this one meets that requirement.  The GTS 3 is very light weight so it feels as if you are not even wearing a watch- This is a plus when you're working out.  The strap feels durable and is not thick and bulky-  Again, a good thing when working out and sweating.  The first thing I noticed when it powered on was the bright and colorful screen.  The colorful display really grabs your attention.  This thing has so many features - It'll take me some time to try everything.  The features that I have looked at and really like are : Altimeter, GPS tracking, blood oxygen, receiving notifications, and the long battery life.  Oh, and you can replace the strap also!  I love it so far!\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  Surprisingly all functions can be on without any premium subscription needed so recommend for those not addicted to certain brands.\n\n",
            "type": "positive"
        },
        {
            "rating": 4,
            "review": "\n\n  Got the gts 3 today. The instruction essentially state pair to your phone, download an app and then proceed. It was not that easy. I had to do many google searches to get enough instructions to change the language from Japanese to English. I would say it took me about 2 hours to complete the setup. Once you are past the initial setup, the watch performs as advertised. Time will tell if it was a good buy.\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  I am very happy with my purchase of the Amazfit as is the ideal smartwatch for fitness.  Besides looking great, the GTS 3 version has all the apps to keep you fit and healthy.  You can measure your heart rate, blood oxygen level even yout stress level. Moreover, it has an app that measures your water intake and another that makes sure you stand up throughout the day. Lasyly its battery life is awesome, since I charged last I am on my 3rd day with 80% battery life.\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  Amazing smartwatch at a great price!!The GTS 3 is stylish, I’ve received so many compliments on it and my friends and family couldn’t believe the price tag. The one tap measuring tracks 4 health metrics in one tap, a great quick overview of my health stats without going through each metric by itself. And the battery life is the best I’ve seen. I can wear my watch to bed and not worry about charging it everyday. I’ve learned so much about my sleeping patterns and have utilized the data from my watch to get better sleep.\n\n",
            "type": "positive"
        }
    ],
    "response": "200"}
     
    ```

3. The result is partionned as follows :
     - Negative_Review [] : Contains all negative reviews with rating < 3
     - Neutral_Review [] : Contains all neutral reviews with rating = 3 
     - Positive_Review [] : Contains all neutral reviews with rating > 3 
                                                                         


<details><summary><b> /Amazon </b></summary>

1. Post Method:
          - **Query Params** :
                    **Url** = "Amazon Product url "

    ``` sh 
     http://127.0.0.1:5000/amazon?url= "url"
    ```

2. Example And Result :
     
     2.1 - Example
     ``` sh 
     http://127.0.0.1:5000/amazon?url= "https://www.amazon.com/Amazfit-Android-Fitness-Display-Tracking/dp/B09H5TWZQT/ref=sr_1_1_sspa?keywords=fitness+GPS&pf_rd_i=21439846011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=67c6cf47-c067-447f-a799-b2cb009a7a6e&pf_rd_r=9QQMNCA3BQF4XZCH232H&pf_rd_s=merchandised-search-8&pf_rd_t=101&qid=1640000071&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQVNEUzY5TEZUT0ROJmVuY3J5cHRlZElkPUEwOTExMTAzM0ZIMVY4QzZDSTNNTCZlbmNyeXB0ZWRBZElkPUEwMTE2NzE5Mk81TFdEVUJDOVhITiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    ```
     2.2 - Result
     
    ``` sh
     {
    "Negative_Review": [
        {
            "rating": 1,
            "review": "\n\n  If you're into fitness please don't get this. I tested it vs known good polar chest strap and Garmin venu and those worked well where the Amafit heartrate couldn't keep up it would make my heartrate randomly dip to 50bpm while my other bands said 140. I got 10 hours of sleep one night and it gave me 6 hours. This is off 3 days of testing and heartrate and sleep tracking were way off.\n\n",
            "type": "negative"
        }
    ],
    "Neutral_Review": [
        {
            "rating": 3,
            "review": "\n\n  Me gusto la forma del producto y las imágenes. También las opciones de medir el stress y el oxigeno. Me ha sido bastante preciso en cuanto al sueño . Me gusta mucho la rotación que tiene el marcador horario, permite ver rápidamente las opciones. Creo que sobrevenden la automatización de los ejercicios. No es automático de pasar de un ejercicio a otro. Tienes que hacer al cambio manual. Recoge bien las caminatas pero si pasas a otro ejercicio por algunos minutos (por ejemplo elíptica) tienes que detenerte y cambiar a elíptica y luego si continuas en caminata tienes que detener elíptica y anotar caminata.  De alguna forma pierdes algo del impulso que llevas. Me preocupa si viajo a Europa con el voltaje 220 porque no podré cambiar de los 110 V de los EUA y en este sentido el reloj es inútil. En ninguna parte menciona como se puede lograr la convertibilidad de 110 V a 220 V.  Para poder emparejar con la app Zepp el proceso fue largo y complicado.  Es muy difícil comunicarse con la casa Amazfit para preguntas y si lo logras no responden.\n\n",
            "type": "neutral"
        }
    ],
    "Positive_Review": [
        {
            "rating": 5,
            "review": "\n\n  My daughter showed me an Amazfit GTR 3 Pro she recently purchased and how easy it was to use, and it looked gorgeous on her.  I needed something that looked stylish while monitoring my heart rate, oxygen level, breathing rate, etc. So we searched upon this brand to see what other watches it has to offer.  And I laid my eyes on this rosa color watch, the screen size is just right, not too big for the wrist, yet I was able to see all the text on the big display.  My daughter helped me set this up in just a few minutes.  And I’ve been wearing it since, received so many compliments from others.  Now I have a piece of mind to track how active I am, and if I were sitting too long, it’d remind me to get up and walk a little.  I also love how it monitors sleep patterns; and suggests ways to reduce stress, such as breathing exercises, to help you improve sleep quality.  The biggest plus is, I had not needed to recharge it since I got the watch (it was at 89% battery when I got it last week); now, almost a week has gone by, it is still running smoothly (you don’t have to charge it daily like the other smartwatches).\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  I purchased the Amazfit GTS 3 to replace my ZTE quartz that died about a year ago. I noticed the GTS 3 is a new model so I decided to try it out.  It's been about a week since I received it and the battery is still going strong.  I've been waiting for a smart watch that does not require charging every day and this one meets that requirement.  The GTS 3 is very light weight so it feels as if you are not even wearing a watch- This is a plus when you're working out.  The strap feels durable and is not thick and bulky-  Again, a good thing when working out and sweating.  The first thing I noticed when it powered on was the bright and colorful screen.  The colorful display really grabs your attention.  This thing has so many features - It'll take me some time to try everything.  The features that I have looked at and really like are : Altimeter, GPS tracking, blood oxygen, receiving notifications, and the long battery life.  Oh, and you can replace the strap also!  I love it so far!\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  Surprisingly all functions can be on without any premium subscription needed so recommend for those not addicted to certain brands.\n\n",
            "type": "positive"
        },
        {
            "rating": 4,
            "review": "\n\n  Got the gts 3 today. The instruction essentially state pair to your phone, download an app and then proceed. It was not that easy. I had to do many google searches to get enough instructions to change the language from Japanese to English. I would say it took me about 2 hours to complete the setup. Once you are past the initial setup, the watch performs as advertised. Time will tell if it was a good buy.\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  I am very happy with my purchase of the Amazfit as is the ideal smartwatch for fitness.  Besides looking great, the GTS 3 version has all the apps to keep you fit and healthy.  You can measure your heart rate, blood oxygen level even yout stress level. Moreover, it has an app that measures your water intake and another that makes sure you stand up throughout the day. Lasyly its battery life is awesome, since I charged last I am on my 3rd day with 80% battery life.\n\n",
            "type": "positive"
        },
        {
            "rating": 5,
            "review": "\n\n  Amazing smartwatch at a great price!!The GTS 3 is stylish, I’ve received so many compliments on it and my friends and family couldn’t believe the price tag. The one tap measuring tracks 4 health metrics in one tap, a great quick overview of my health stats without going through each metric by itself. And the battery life is the best I’ve seen. I can wear my watch to bed and not worry about charging it everyday. I’ve learned so much about my sleeping patterns and have utilized the data from my watch to get better sleep.\n\n",
            "type": "positive"
        }
    ],
    "response": "200"}
     
    ```

3. The result is partionned as follows :
     - Negative_Review [] : Contains all negative reviews with rating < 3
     - Neutral_Review [] : Contains all neutral reviews with rating = 3 
     - Positive_Review [] : Contains all neutral reviews with rating > 3 
                                                                         

