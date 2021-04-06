class Puhelinluettelo:
    def __init__(self) -> None:
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if nimi not in self.__henkilot:
            # The person is associated with a list of phone numbers
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

    def suorita(self):
        self.ohje()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                break


# testikoodia
if __name__ == '__main__':
    luettelo = Puhelinluettelo()
    luettelo.lisaa_numero("Erkki", "02-123456")
    print(luettelo.hae_numerot("Erkki"))
    print(luettelo.hae_numerot("Emilia"))
