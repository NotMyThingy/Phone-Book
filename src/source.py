class Puhelinluettelo:
    def __init__(self) -> None:
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_osoite(osoite)

    def tiedot(self, nimi: str):
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


class Henkilo:
    def __init__(self, nimi: str) -> None:
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = ''

    def nimi(self):
        return self.__nimi

    def numerot(self):
        return self.__numerot

    def osoite(self):
        if not self.__osoite:
            return None

        return self.__osoite

    def lisaa_numero(self, numero: str):
        if not numero:
            return

        self.__numerot.append(numero)

    def lisaa_osoite(self, osoite: str):
        if not osoite:
            return

        self.__osoite = osoite

    def __str__(self) -> str:
        return f'{self.__nimi}\n  {", ".join(self.__numerot)}\n  {self.osoite()}'


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
        print('1 - nimen lisäys')
        print('2 - osoiteen lisäys')
        print('3 - haku')
        print('4 - haku numeron perusteella')

    # uusien tietojen lisääminen
    def nimen_lisays(self):
        nimi = input('nimi: ')
        numero = input('numero: ')
        self.__luettelo.lisaa_numero(nimi, numero)

    # osoiteen lisääminen tietoihin
    def osoiteen_lisays(self):
        nimi = input('nimi: ')
        osoite = input('osoite: ')
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input('nimi: ')
        haettu = self.__luettelo.tiedot(nimi)
        if haettu == None:
            print('numero ei tiedossa')
            return

        for numero in haettu.numerot():
            print(numero)

        if not haettu.osoite():
            print('osoite ei tiedossa')
        else:
            print(haettu.osoite())

    # def haku_numerolla(self):
    #     numero = input('numero: ')
    #     nimi = self.__luettelo.hae_numerolla(numero)
    #     if nimi == None:
    #         print('tuntematon numero')
    #     else:
    #         print(nimi)

    #def lopetus(self):
    #  self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())

    def suorita(self):
        self.ohje()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                self.lopetus()
                break

            if komento == '1':
                self.nimen_lisays()
            elif komento == '2':
                self.osoiteen_lisays()
            elif komento == '3':
                self.haku()
            elif komento == '4':
                self.haku_numerolla()
            else:
                self.ohje()


# testikoodia
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
