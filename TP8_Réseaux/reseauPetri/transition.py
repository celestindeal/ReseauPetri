

class Transition():

    def __init__(self, nom) -> None:
        self._nom = nom
        self._conditions = {}
        self._actions = {}
        pass

    def addCondition(self, place, jetons):
        self._conditions[place] = jetons

    def addAction(self, place, jetons):
        self._actions[place] = jetons