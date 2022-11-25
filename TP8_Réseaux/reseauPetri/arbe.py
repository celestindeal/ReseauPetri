

class Arbre ():


    def __init__(self,nom) -> None:
        self._nom = nom
        self.listPlaces = []
        pass

    def addPlace(self,place):
        self.listPlaces.append(place)