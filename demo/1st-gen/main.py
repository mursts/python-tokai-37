import requests
import requests_toolbelt.adapters.appengine
from flask import Flask

requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/api/weather')
def weather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=230010'
    r = requests.get(url)
    # print(r.context)
    return r.content
