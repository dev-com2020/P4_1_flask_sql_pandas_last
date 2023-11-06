import urllib.parse
import urllib.request
import feedparser
from flask import Flask, render_template, request, typing as ft
import json

from flask.views import View, MethodView

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

DEFAULTS = {'publication': 'bbc', 'city': 'London,UK', 'currency_from': 'USD', 'currency_to': 'PLN'}
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=cb932829eacb6a0e9ee4f38bfbf112ed"
CURRENCY_URL = 'https://openexchangerates.org//api/latest.json?app_id=b23c94daab584f4580e4e2bf75cbcf7e'


def get_rate(frm, to):
    all_currency = urllib.request.urlopen(CURRENCY_URL).read()
    parsed = json.loads(all_currency).get('rates')
    frm_rate = parsed.get(frm.upper())
    to_rate = parsed.get(to.upper())
    return to_rate / frm_rate, parsed.keys()


@app.route("/")
def home():
    publication = request.args.get("publication")
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    currency_from = request.args.get("currency_from")
    if not currency_from:
        currency_from = DEFAULTS['currency_from']
    currency_to = request.args.get("currency_to")
    if not currency_to:
        currency_to = DEFAULTS['currency_to']
    rate, currencies = get_rate(currency_from, currency_to)
    return render_template("news.html", articles=articles, weather=weather)


def get_weather(query):
    query = urllib.parse.quote(query)
    url = WEATHER_URL.format(query)
    response = urllib.request.urlopen(url)
    data = response.read()
    parsed = json.loads(data.decode('utf-8'))
    weather = None
    if parsed.get("weather"):
        weather = {"description": parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   "country": parsed['sys']['country']}
    return weather


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


# def get_request():
#     bar = request.args.get('foo', 'bar')
#     return 'Prosta trasa Flaska gdzie foo jest %s' % bar
#
#
# app.add_url_rule('/get-req', view_func=get_request)


@app.route('/post-req', methods=['POST'])
def post_request():
    bar = request.form.get('foo', 'bar')
    return 'Prosta trasa Flaska gdzie foo jest %s' % bar


@app.route('/a-req', methods=['GET', 'POST'])
def some_request():
    if request.method == 'GET':
        bar = request.args.get('foo', 'bar')
    else:
        bar = request.form.get('foo', 'bar')
    return 'Prosta trasa Flaska gdzie foo jest %s' % bar


class GetRequest(View):
    def dispatch_request(self):
        bar = request.args.get('foo', 'bar')
        return 'Prosta trasa Flaska gdzie foo jest %s' % bar


class GetPostRequest(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'GET':
            bar = request.args.get('foo', 'bar')
        if request.method == 'POST':
            bar = request.form.get('foo', 'bar')
        return 'Prosta trasa Flaska gdzie foo jest %s' % bar


class GetPostRequest2(MethodView):

    def get(self):
        bar = request.args.get('foo', 'bar')
        return 'Prosta trasa Flaska gdzie foo jest %s' % bar
    def post(self):
        bar = request.form.get('foo', 'bar')
        return 'Prosta trasa Flaska gdzie foo jest %s' % bar


# @app.route('/test/<name>')
# def get_name(name):
#     return name

@app.route('/test/<string(minlength=2,maxlength=3):code>')
def get_name(code):
    return code

@app.route('/test/<int(min=18,max=99):age>')
def get_age(age):
    return str(age)



app.add_url_rule('/a-get-req', view_func=GetRequest.as_view('get_request'))
app.add_url_rule('/a-req', view_func=GetPostRequest.as_view('a_request'))
app.add_url_rule('/a-req2', view_func=GetPostRequest2.as_view('a_request2'))

if __name__ == '__main__':
    app.run(debug=True, port=5666)
