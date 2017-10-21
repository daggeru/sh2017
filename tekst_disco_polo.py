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

    def wrzucanie_do_jsona(self):
        piosenka = {
            'zwrotki': [],
            'refren': []
        }

        for i in range(0, 4):
            piosenka['zwrotki'].append(random.choice(self.wersy))
        for i in range(0, 4):
            piosenka['refren'].append(random.choice(self.wersy))
        return piosenka

    def generator_tekstu(self):
        str = ""
        for wers in self.wersy:
            str += (''.join(wers))
        return str


instancja = TekstDiscoPolo()
instancja.wczytaj_tekst('tekst_disco.txt')

# print(wersy)
# print(instancja.generator_tekstu())
print(instancja.wrzucanie_do_jsona())
