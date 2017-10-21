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
            ['pierwsza linijka1', 'druga linijka1', 'trzecia linijka1', 'czwarta linijka1'],
            ['pierwsza linijka2', 'druga linijka2', 'trzecia linijka2', 'czwarta linijka2'],
            ['pierwsza linijka3', 'druga linijka3', 'trzecia linijka3', 'czwarta linijka3'],
        ],
        'refren': [
            ['pierwsza linijka refrenu', 'druga linijka refrenu', 'trzecia linijka refrenu', 'czwarta linijka refrenu'],
        ]
    }
    return json.dumps(tekst)


if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, app)
    print("Serving on port %s..." % port)
    httpd.serve_forever()
