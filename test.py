import random
import pandas
import utility
from ner import ner
from summary import summary

df = pandas.read_csv('dataset_tweet_sentiment_opini_film.csv', delimiter=',')
tweets = df['Text Tweet']
count_tweet = len(tweets)

for tweet in range(10):
    text = tweets[random.randint(0, count_tweet)]
    print("Original Text : ")
    print(text)
    text = utility.removeURL(text)
    text = utility.removeSpecialChar(text)
    text = utility.removeEmoji(text)
    text = utility.removeDoubleSpace(text)
    print("Clean Text : ")
    print(text)
    print("Extract Entity : ")
    print(ner(text))
    print("Extract Summary : ")
    print(summary(text))
    print("=====================================")