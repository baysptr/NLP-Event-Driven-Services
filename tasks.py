from ner import ner
from senti import analytics
from summary import summary
from words import wordCloud
from utility import postCallback
import time

def entityExtract(text):
    data = text.to_dict()
    print("Starting task: Entity Extractor")
    time.sleep(1)

    entity = ner(data['data'])
    print(postCallback(url=data['callback'], id=data['id'], data=entity))

    time.sleep(1)
    print("Task completed: Entity Extractor")

def sentimentAnalytics(text):
    data = text.to_dict()
    print("Starting task: Sentiment Extractor")
    time.sleep(1)

    sentiment = analytics(data['data'])
    print(postCallback(url=data['callback'], id=data['id'], data=sentiment))

    time.sleep(1)
    print("Task completed: Sentiment Extractor")

def summaryAnalytics(text):
    data = text.to_dict()
    print("Starting task: Summary Extractor")
    time.sleep(1)

    resume = summary(data['data'])
    print(postCallback(url=data['callback'], id=data['id'], data=resume))

    time.sleep(1)
    print("Task completed: Summary Extractor")

def wordClouds(text):
    data = text.to_dict()
    print("Starting task: Words Extractor")
    time.sleep(1)

    words = wordCloud(data['data'])
    print(postCallback(url=data['callback'], id=data['id'], data=words))

    time.sleep(1)
    print("Task completed: Words Extractor")