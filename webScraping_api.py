from urllib.request import urlopen
from bs4 import BeautifulSoup

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps


def scrapingBianca():
    url = "http://bianca.com/"

    html = urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    name = soup.title.text
    title = soup.h1.text

    data = {
        "site_name": name,
        "site_title": title
    }

    return data


class BiancaScraping(Resource):
    def get(self):
        data = scrapingBianca()
        return jsonify(data)


app = Flask(__name__)
api = Api(app)

api.add_resource(BiancaScraping, '/getBiancaData')

if __name__ == '__main__':
    app.run()
