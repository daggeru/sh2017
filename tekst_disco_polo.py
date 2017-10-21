import random


class TekstDiscoPolo:
    def __init__(self):
        self.wersy = []

    def wczytaj_tekst(self, plik):
        plik = open(plik, 'r')
        linijki_tekstu = plik.readlines()
        self.wersy = []
        for linijka in linijki_tekstu:
            linijka = linijka.rstrip()
            if not linijka == '':
                self.wersy.append(linijka)

    def generuj_piosenke(self, ilosc_zwrotek=4):
        piosenka = {
            'refren': [],
            'zwrotki': []
        }

        zwrotki = []
        for i in range(ilosc_zwrotek):
            zwrotka = []
            for i in range(0, 4):
                zwrotka.append(random.choice(self.wersy))
            zwrotki.append(zwrotka)
        piosenka['zwrotki'] = zwrotki
        for i in range(0, 4):
            piosenka['refren'].append(random.choice(self.wersy))
        return piosenka

    def generator_tekstu(self):
        str = ""
        for wers in self.wersy:
            str += (''.join(wers))
        return str

#
#
# instancja = TekstDiscoPolo()
#
# instancja.wczytaj_tekst('tekst_disco.txt')
