class GenerujTekstDiscoPolo:
    def __init(self, pusta_lista):
        self.pusta_lista = pusta_lista

    def wczytaj_tekst(self, plik):
        plik = open(plik, 'r')
        linijki_tekstu = plik.readlines()
        self.pusta_lista = []
        for linijka in linijki_tekstu:

            self.pusta_lista.append(linijka)
        return self.pusta_lista



instancja = GenerujTekstDiscoPolo()
print(instancja.wczytaj_tekst('tekst_disco.txt'))