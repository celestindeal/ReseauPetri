

from TP8_Réseaux.reseauPetri.transition import Transition


class Petri():

    def __init__(self, nom ):
        self._nom = nom
        self._listPlaces = []
        self._listTransitions = []
        pass

    def addPlace(self,place):
        self._listPlaces.append(place)

    def addTransition(self, nom, condition, action):
        
        for place in condition:
            if place not in self._listPlaces:
                return False
        for place in action:
            if place not in self._listPlaces:
                return False
        self._listTransitions.append(Transition(nom, condition, action))