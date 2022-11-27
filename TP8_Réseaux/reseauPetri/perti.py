

class Transition():

    def __init__(self, nom, condition, action) -> None:
        self._nom = nom
        self._conditions = condition
        self._actions = action
        pass

    def addCondition(self, place, jetons):
        self._conditions[place] = jetons

    def addAction(self, place, jetons):
        self._actions[place] = jetons


class Petri():

    def __init__(self, nom ):
        self._nom = nom
        self._listPlaces = []
        self._listTransitions = []
        pass

    def printreseauPetri(self):
        print("reseauPetri: " + self._nom)
        print("Places:")
        for place in self._listPlaces:
            print(place._nom)
        print("Transitions:")
        for transition in self._listTransitions:
            print(transition._nom)
            print("\t"+"Conditions:")
            for place in transition._conditions:
                print("\t"+place._nom + ": " + str(transition._conditions[place]))
            print("\t"+"Actions:")
            for place in transition._actions:
                print("\t"+place._nom + ": " + str(transition._actions[place]))
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

    def buildArbre(self):
        pass