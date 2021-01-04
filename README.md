### nlp-sentiment-scent-coronavirus
## Project: Have Reviews of Yankee Candle Products Been Impacted by the Coronavirus Pandemic?

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

**Objective:** Use natural language processing and sentiment analysis to research the impact of the coronavirus pandemic on the review of Yankee Candle products on Amazon.

**Hypothesis:** That average review ratings and sentiment for Yankee Candle products on Amazon have decreased in 2020, when compared to previous years, due to the common coronavirus sympton of a loss of smell. My assertion is that purchasers of Yankee Candles blame the manufacturer for a lack of scent in the product, without realizing it is their own health condition that is at fault.

**Tools Used:** Python, Pandas, Scrapy, NLTK, Gensim, TextBlob, VADER Sentiment Analysis, scikit-learn, Matplotlib, Seaborn

**Skills Demonstrated:** Web Scraping, Data Cleaning, Feature Extraction, Exploratory Data Analysis, Natural Language Processing (Sentiment Analysis, Topic Modelling), Data Visualization

**Conclusions:**

Based on the analysis performed, we can accept the hypothesis that the review ratings and sentiment for Yankee Candle products on Amazon have decreased in 2020, when compared to previous years and this is likely due to the common coronavirus symptom of a loss of smell.

My conclusion is based on the following observations and insights from my analysis:
* There is a clear and significant decrease in good reviews for Yankee Candle products and a corresponding increase in bad reviews beginning in April 2020.  In July 2020 there were almost an equal number of good reviews and bad reviews for Yankee Candle products, for the first and only time.
* It can be seen from April to September 2020 that the gap between the number of good reviews for Yankee Candle products and the number of bad reviews narrows, when compared to earlier months.  History shows that there are usually substantially more good reviews than bad reviews for Yankee Candle products on Amazon.
* There is an obvious deterioration in the average review rating for Yankee Candle products in 2020, from the onset of the coronavirus pandemic. Review ratings have dropped from an average of nearly 4.5 in January 2020 to between 3.3 and 3.6 in the subsequent months.
* The average VADER positive, neutral and negative scores remain relatively stable until 2020, when the positive score starts to trend down and both the neutral and negative scores trend up. This is a reflection of the overall decrease in sentiment expressed in the reviews of Yankee Candle products on Amazon in 2020.
* It is evident that there is a material shift to the left in the distribution of the sentiment of reviews during the pandemic when compared to before the pandemic. This is consistent with the decrease in the average review ratings.
* Four of the top 50 bigrams/trigrams in Yankee Candle product reviews on Amazon before the coronavirus pandemic relate to a lack of scent (scent not, no scent, not strong, not smell), whereas 7 of the top 50 in product reviews during the pandemic relate to a lack of scent (no scent, scent not, not strong, not smell, no smell, barely smell, smell not).  The ratio of the lack of scent ngrams appearing in product reviews before the pandemic is 1,255 occurences of the ngrams to 20,806 product reviews (0.06:1), whereas during the pandemic the ratio is 1,097 occurences of the ngrams to 10,315 product reviews (0.11:1).
