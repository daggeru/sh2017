from flask import Flask
from flask import render_template
from tekst_disco_polo import TekstDiscoPolo
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Strona Tytułowa')


@app.route('/generuj')
def generuj():
    tekst = TekstDiscoPolo()
    tekst.wczytaj_tekst('tekst_disco.txt')
    tekst_dict = tekst.wrzucanie_do_jsona()
    tekst_dict = {
        'zwrotki': [
            ['pierwsza linijka1', 'druga linijka1', 'trzecia linijka1', 'czwarta linijka1'],
            ['pierwsza linijka2', 'druga linijka2', 'trzecia linijka2', 'czwarta linijka2'],
            ['pierwsza linijka3', 'druga linijka3', 'trzecia linijka3', 'czwarta linijka3'],
        ],
        'refren': [
            'pierwsza linijka refrenu',
            'druga linijka refrenu',
            'trzecia linijka refrenu',
            'czwarta linijka refrenu'
        ]
    }
    return json.dumps(tekst_dict)


if __name__ == '__main__':
    app.run(debug=True)
