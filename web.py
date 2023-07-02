from datetime import timedelta
from flask import Flask, jsonify, request
from redis import Redis
from rq import Queue
import tasks

queue = Queue(connection=Redis())
app = Flask(__name__)

@app.route('/')
def default():
    return jsonify({'msg': 'Hello Wordl!'})

@app.route('/entity-extract', methods=['POST'])
def entityExtract():
    formData = request.form
    queue.enqueue_in(timedelta(seconds=3), tasks.entityExtract, formData)

    return jsonify(formData.to_dict())


@app.route('/sentiment-analytic', methods=['POST'])
def entityExtract():
    formData = request.form
    queue.enqueue_in(timedelta(seconds=6), tasks.sentimentAnalytics, formData)

    return jsonify(formData.to_dict())

@app.route('/summary-extract', methods=['POST'])
def entityExtract():
    formData = request.form
    queue.enqueue_in(timedelta(seconds=9), tasks.summaryAnalytics, formData)

    return jsonify(formData.to_dict())

@app.route('/word-cloud', methods=['POST'])
def entityExtract():
    formData = request.form
    queue.enqueue_in(timedelta(seconds=12), tasks.wordClouds, formData)

    return jsonify(formData.to_dict())

if __name__ == '__main__':
    app.run(port=1111)