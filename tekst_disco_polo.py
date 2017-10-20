class TekstDiscoPolo:
    def __init__(self, wersy):
        self.wersy = wersy

    def wczytaj_tekst(self, plik):
        plik = open(plik, 'r')
        linijki_tekstu = plik.readlines()
        self.wersy = []
        for linijka in linijki_tekstu:
            self.wersy.append(linijka.split())
        for lista in self.wersy:
            if lista ==[]:
                self.wersy.remove([])
        return self.wersy


instancja = TekstDiscoPolo()
print(instancja.wczytaj_tekst('tekst_disco.txt'))