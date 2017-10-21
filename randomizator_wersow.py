import random
import re
import przymiotniki


class RandomizatorWersow:
    ustawienia = {
        'otak': 0.3
    }

    def otak(self, wers):
        if random.random() < self.ustawienia['otak']:
            return wers + ', o tak!'
        else:
            return wers

    def zamien_przymiotniki(self, wers):
        wers = re.sub(r"<p_n>", random.choice(przymiotniki.przymiotniki_n), wers)
        wers = re.sub(r"<p_k>", random.choice(przymiotniki.przymiotniki_k), wers)
        return wers

    def randomizuj_wers(self, wers):
        randomizatory = []
        randomizatory.append(self.otak)
        randomizatory.append(self.zamien_przymiotniki)

        for randomizator in randomizatory:
            wers = randomizator(wers)
        return wers

#
# r = RandomizatorWersow()
# wers = 'Tak zakochać, zakochać się można tylko raz'
# wynik = r.randomizuj_wers(wers)
# print(wynik)
