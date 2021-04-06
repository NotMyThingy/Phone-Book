class Puhelinluettelo:
    def __init__(self) -> None:
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if nimi not in self.__henkilot:
            self.__henkilot[nimi] = []

        self.__henkilot[nimi].append(numero)

    def hae_numerot(self, nimi: str):
        if nimi not in self.__henkilot:
            return None

        return self.__henkilot[nimi]


class PuhelinluetteloSovellus:
    def __init__(self) -> None:
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print('komennot:')
        print('0 - lopetus')
        print('1 - lisäys')
        print('2 - haku')

    # uusien tietojen lisääminen
    def lisays(self):
        nimi = input('nimi: ')
        numero = input('numero: ')
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input('nimi: ')
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot is None:
            print('numero ei tiedossa')
            return

        for numero in numerot:
            print(numero)

    def suorita(self):
        self.ohje()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                break

            if komento == '1':
                self.lisays()
            elif komento == '2':
                self.haku()


class Tiedostonkasittelija:
    def __init__(self, tiedosto: str) -> None:
        self.__tiedosto = tiedosto

    def lataa(self):
        nimet = {}
        with open(self.__tiedosto) as t:
            for rivi in t:
                osat = rivi.strip().split(';')
                nimi, *numerot = osat
                nimet[nimi] = numerot

        return nimet


# testikoodia
if __name__ == '__main__':
    t = Tiedostonkasittelija("luettelo.txt")
    print(t.lataa())
