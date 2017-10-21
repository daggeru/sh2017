import random
class TekstDiscoPolo:
    def __init__(self, wersy):
        self.wersy = wersy

    def wczytaj_tekst(self, plik):
        plik = open(plik, 'r')
        linijki_tekstu = plik.readlines()
        self.wersy = []
        for linijka in linijki_tekstu:
            self.wersy.append(linijka.rstrip())
        for lista in self.wersy:
            if lista ==[] and lista=="":
                self.wersy.remove([])
                self.wersy.remove("")
        return self.wersy

    def wrzucanie_do_jsona(self, wersy):
        json = {
            'zwrotki':[],
            'refren':[]
        }

        for i in range(0,4):
            json['zwrotki'].append(random.choice(wersy))
        for i in range(0,4):
            json['refren'].append(random.choice(wersy))
        return json


    def generator_tekstu(self, wersy):
        str = ""
        for wers in wersy:
            str += (''.join(wers))
        return str

instancja = TekstDiscoPolo([])
wersy = instancja.wczytaj_tekst('tekst_disco.txt')
# print(wersy)
# print(instancja.generator_tekstu(wersy))
# print(instancja.wrzucanie_do_jsona(wersy))