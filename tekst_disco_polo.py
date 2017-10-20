class TekstDiscoPolo:
    def __init__(self, wersy):
        self.wersy = wersy

    def wczytaj_tekst(self, plik):
        plik = open(plik, 'r')
        linijki_tekstu = plik.readlines()
        self.wersy = []
        for linijka in linijki_tekstu:
            self.wersy.append(linijka)
        for lista in self.wersy:
            if lista ==[]:
                self.wersy.remove([])
        return self.wersy

    def generator_tekstu(self, wersy):
        str = ""
        for wers in wersy:
            str += (''.join(wers))
        return str

instancja = TekstDiscoPolo([])
wersy = instancja.wczytaj_tekst('tekst_disco.txt')
# print(wersy)
print(instancja.generator_tekstu(wersy))