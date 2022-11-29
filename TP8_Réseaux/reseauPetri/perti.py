from .arbre import Arbre
from .noeud import Noeud
from .transition import Transition


class Petri():

    def __init__(self, nom ):
        """
        constructeur
        """
        self._nom = nom
        self._listPlaces = []
        self._listTransitions = []
        self._arbre = Arbre(nom)
        self._places_arrivee = []
        self._place_temps = None
        self._minimum = 9999
        pass

    def printreseauPetri(self):
        print("reseauPetri: " + self._nom)
        print("Places:")
        for place in self._listPlaces:
            print(place._nom, ":", place._jetons)
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
    

    def findJetons(self):
        placesAvecJetons = []
        for place in self._listPlaces:
            if place._jetons > 0:
                placesAvecJetons.append(place)
        return placesAvecJetons


    def findTransitionsPossibles(self):
        transitionsPossibles = []
        for t in self._listTransitions:
            check = True
            for key in t._conditions:
                if key._jetons < t._conditions[key]:
                    check = False
            if check:
                transitionsPossibles.append(t)
        return transitionsPossibles

    def buildArbre(self):
        # init
        marquageInit = self.findJetons()
        n = Noeud(None)
        for place in marquageInit:
            n.addValue(place._nom, place._jetons)
        self._arbre.addNoeud(n, None)

        self.parcoursArbre(self._arbre._listNoeud[0], 1)

        #print("\nArbre:", self._arbre._nom)
        #self._arbre.printArbre()

    
    def parcoursArbre(self, antecedent, nb):

        tp = self.findTransitionsPossibles()

        tp_str = ""
        for t in tp:
            tp_str += t._nom

        # parcours des transitions possibles
        for t in tp:

            # execution de la transition
            t.execTransition()

            # créé un nouveau noeud avec le nouveau marquage
            marquage = self.findJetons()
            n = Noeud(antecedent)
            for place in marquage:
                n.addValue(place._nom, place._jetons)
            # TP8 exo 2 : trouver le noeud d'arrivée avec le temps minimum
            check = True
            for place_arrivee in self._places_arrivee:
                if place_arrivee._nom not in n._valeurs.keys():
                    check = False
            if check and self._minimum > self._place_temps._jetons:
                self._minimum = self._place_temps._jetons
            

            # ajoute le nouveau noeud à l'arbre
            if not self._arbre.addNoeud(n, t) and not self._arbre.isGenerator(n, t):
                # recursivite si pas d'antecedent pareil
                self.parcoursArbre(n, nb+1)

            t.inverserTransition()


    def IsReseauBorne(self):
        return self._arbre._isBorne
