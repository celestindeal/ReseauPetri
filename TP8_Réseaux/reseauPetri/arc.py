from .noeud import Noeud

class Arc():

    def __init__(self, na:Noeud, ns:Noeud, t:str):
        self._noeudAntecedent = na
        self._noeudSuivant = ns
        self._nomTransition = t
    
    def toString(self):
        return self._noeudAntecedent.toString() + " -" + self._nomTransition + "-> " + self._noeudSuivant.toString()