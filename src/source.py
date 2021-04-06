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

    def hae_numerolla(self, numero: str):
        for nimi, numerot in self.__henkilot.items():
            if numero in numerot:
                return nimi

        return None

    def kaikki_tiedot(self):
        return self.__henkilot


class PuhelinluetteloSovellus:
    def __init__(self) -> None:
        self.__luettelo = Puhelinluettelo()
        self.__tiedosto = Tiedostonkasittelija('luettelo.txt')

        for nimi, numerot in self.__tiedosto.lataa().items():
            for numero in numerot:
                self.__luettelo.lisaa_numero(nimi, numero)

    def ohje(self):
        print('komennot:')
        print('0 - lopetus')
        print('1 - lisäys')
        print('2 - haku')
        print('3 - haku numeron perusteella')

    # uusien tietojen lisääminen
    def lisays(self):
        nimi = input('nimi: ')
        numero = input('numero: ')
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input('nimi: ')
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print('numero ei tiedossa')
            return

        for numero in numerot:
            print(numero)

    def haku_numerolla(self):
        numero = input('numero: ')
        nimi = self.__luettelo.hae_numerolla(numero)
        if nimi == None:
            print('tuntematon numero')
        else:
            print(nimi)

    def lopetus(self):
        self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())

    def suorita(self):
        self.ohje()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                self.lopetus()
                break

            if komento == '1':
                self.lisays()
            elif komento == '2':
                self.haku()
            elif komento == '3':
                self.haku_numerolla()
            else:
                self.ohje()


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

    def talleta(self, luettelo: dict):
        with open(self.__tiedosto, 'w') as t:
            for nimi, numerot in luettelo.items():
                rivi = [nimi] + numerot
                t.write(';'.join(rivi) + '\n')


# testikoodia
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
