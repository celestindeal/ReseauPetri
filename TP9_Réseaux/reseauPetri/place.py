

class Place():

    def __init__(self,nom,jeton,placeAntecedant,placeSuivant) -> None:
        self._nom = nom
        self._placeAntecedant = placeAntecedant
        self._placeSuivant = placeSuivant
        self._jetons = jeton

    def addPlaceAntecedant(self,placeAntecedant):
        self._placeAntecedant = placeAntecedant

    def addPlaceSuivant(self,placeSuivant):
        self._placeSuivant = placeSuivant

