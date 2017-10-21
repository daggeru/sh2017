from flask import Flask
from flask import render_template
from wsgiref.simple_server import make_server
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Strona Tytułowa')


<<<<<<< HEAD
class GeneratorPiosenki:
    def on_get(self, req, resp):
        tekst = {
            'zwrotki''tekst_disco.txt': [
                'pierwsza linijka#1\ndruga linijka#1\ntrzecia linijka#1\nczwarta linijka#1',
                'pierwsza linijka#2\ndruga linijka#2\ntrzecia linijka#2\nczwarta linijka#2',
                'pierwsza linijka#3\ndruga linijka#3\ntrzecia linijka#3\nczwarta linijka#3'
            ],
            'refreny': [
                'pierwsza linijkaREF#1\ndruga linijkaREF#1\ntrzecia linijkaREF#1\nczwarta linijkaREF#1',
                'pierwsza linijkaREF#2\ndruga linijkaREF#2\ntrzecia linijkaREF#2\nczwarta linijkaREF#2'
            ]
        }
=======
@app.route('/generuj')
def generuj():
    tekst = {
        'zwrotki': [
            ['pierwsza linijka1', 'druga linijka1', 'trzecia linijka1', 'czwarta linijka1'],
            ['pierwsza linijka2', 'druga linijka2', 'trzecia linijka2', 'czwarta linijka2'],
            ['pierwsza linijka3', 'druga linijka3', 'trzecia linijka3', 'czwarta linijka3'],
        ],
        'refren': [
            ['pierwsza linijka refrenu', 'druga linijka refrenu', 'trzecia linijka refrenu', 'czwarta linijka refrenu'],
        ]
    }
    return json.dumps(tekst)
>>>>>>> b53a3dbb42fe1067cc621d6d8b00e54b68a11e93


if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, app)
    print("Serving on port %s..." % port)
    httpd.serve_forever()
