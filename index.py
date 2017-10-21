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
    tekst_dict = tekst.generuj_piosenke(4)
    return json.dumps(tekst_dict)


if __name__ == '__main__':
    app.run(debug=True)
