from flask import Flask
from flask import render_template
from wsgiref.simple_server import make_server
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Strona Tytułowa')


@app.route('/generuj')
def generuj():
    tekst = {
        'zwrotki': [
            'pierwsza linijka#1\ndruga linijka#1\ntrzecia linijka#1\nczwarta linijka#1',
            'pierwsza linijka#2\ndruga linijka#2\ntrzecia linijka#2\nczwarta linijka#2',
            'pierwsza linijka#3\ndruga linijka#3\ntrzecia linijka#3\nczwarta linijka#3'
        ],
        'refreny': [
            'pierwsza linijkaREF#1\ndruga linijkaREF#1\ntrzecia linijkaREF#1\nczwarta linijkaREF#1',
            'pierwsza linijkaREF#2\ndruga linijkaREF#2\ntrzecia linijkaREF#2\nczwarta linijkaREF#2'
        ]
    }
    return json.dumps(tekst)


if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, app)
    print("Serving on port %s..." % port)
    httpd.serve_forever()
