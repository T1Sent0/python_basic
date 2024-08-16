import json
from flask import Flask
import requests
import os


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table style="border-collapse: collapse">'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td style="border: 1px solid #c4c4c4; padding: 10px">{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run(), '(', os.name, ')'