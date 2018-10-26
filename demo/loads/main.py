#!/usr/bin/env python

import datetime
import logging

from flask import Flask
from flask.json import jsonify
from google.appengine.ext import ndb

app = Flask(__name__)


class Greeting(ndb.Model):
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls):
        return cls.query().order(-cls.date)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/read', methods=['GET'])
def read():
    greetings = Greeting.query_book().fetch(20, keys_only=True)
    greetings = ndb.get_multi(greetings)

    result = [dict(content=greeting.content, date=greeting.date) for greeting in greetings]

    return jsonify(result)


@app.route('/write', methods=['POST'])
def write():
    content = datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
    greeting = Greeting(content=content)
    greeting.put()

    return 'write done'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
