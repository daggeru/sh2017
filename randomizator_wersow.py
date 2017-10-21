import random
import re

from wyrazy import przymiotniki, rzeczowniki


class RandomizatorWersow:
    ustawienia = {
        'otak': 0.2,
        'no_i_czesc': 0.2
    }

    def otak(self, wers):
        if random.random() < self.ustawienia['otak']:
            return wers + ', o tak!'
        else:
            return wers

    def no_i_czesc(self, wers):
        if random.random() < self.ustawienia['no_i_czesc']:
            return wers + ', no i cześć!'
        else:
            return wers

    def wstaw_wyraz(self, wers):
        wers = re.sub(r"<p_n>", random.choice(przymiotniki.przymiotniki_n), wers)
        wers = re.sub(r"<p_k>", random.choice(przymiotniki.przymiotniki_k), wers)
        for _ in range(len(re.findall(r"<r>", wers))):
            wers = re.sub(r"<r>", random.choice(rzeczowniki.rzeczowniki), wers)
        return wers

    def randomizuj_wers(self, wers):
        randomizatory = [
            self.otak,
            self.no_i_czesc,
            self.wstaw_wyraz
        ]

        for randomizator in randomizatory:
            wers = randomizator(wers)
        return wers

#
# r = RandomizatorWersow()
# wers = 'Tak zakochać, zakochać się można tylko raz'
# wynik = r.randomizuj_wers(wers)
# print(wynik)
