from .arbre import Arbre
from .noeud import Noeud
from .graph import Graph
from .transition import Transition
from .arc import Arc


class Petri():

    def __init__(self, nom ):
        """
        constructeur
        """
        self._nom = nom
        self._listPlaces = []
        self._listTransitions = []
        self._arbre = Arbre(nom)
        self._graph = Graph(nom)
        self._bloquant = False
        self._marquageBloque = []
        self._propre = True
        self._transitionsParcourues = []
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
    
    ###############################  Gestion de l'arbre ###############################        

    def buildArbre(self):
        # init
        marquageInit = self.findJetons()
        n = Noeud(None)
        for place in marquageInit:
            n.addValue(place._nom, place._jetons)
        self._arbre.addNoeud(n, None)

        self.parcoursArbre(self._arbre._listNoeud[0], 1)

    def parcoursArbre(self, antecedent, nb):

        tp = self.findTransitionsPossibles()
        if len(tp) == 0:
            self._bloquant = True
            # créé le marquage actuel
            marquage = self.findJetons()
            n = Noeud(antecedent)
            for place in marquage:
                n.addValue(place._nom, place._jetons)
            self._marquageBloque.append(n.toString())
            return

        # parcours des transitions possibles
        for t in tp:

            # execution de la transition
            t.execTransition()
            if t not in self._transitionsParcourues:
                self._transitionsParcourues.append(t)

            # créé un nouveau noeud avec le nouveau marquage
            marquage = self.findJetons()
            n = Noeud(antecedent)
            for place in marquage:
                n.addValue(place._nom, place._jetons)

            # ajoute le nouveau noeud à l'arbre
            if not self._arbre.addNoeud(n, t) and not self._arbre.isGenerator(n, t):
                # recursivite si pas d'antecedent pareil
                self.parcoursArbre(n, nb+1)

            t.inverserTransition()
            
    def printArbre(self):
        print("\nArbre:", self._arbre._nom)
        self._arbre.printArbre()
        
        
    ###############################  Gestion du graph ###############################        
    def buildGraph(self):
        # init
        marquageInit = self.findJetons()
        n = Noeud(None)
        for place in marquageInit:
            n.addValue(place._nom, place._jetons)
        self._graph._listNoeud.append(n)

        self.parcoursGraph(self._graph._listNoeud[0], 1)

    def parcoursGraph(self, antecedent, nb):

        tp = self.findTransitionsPossibles()
        if len(tp) == 0:
            self._bloquant = True
            # créé le marquage actuel
            marquage = self.findJetons()
            n = Noeud(antecedent)
            for place in marquage:
                n.addValue(place._nom, place._jetons)
            self._marquageBloque.append(n.toString())
            return

        # parcours des transitions possibles
        for t in tp:

            # execution de la transition
            t.execTransition()
            if t not in self._transitionsParcourues:
                self._transitionsParcourues.append(t)

            # créé un nouveau noeud avec le nouveau marquage
            marquage = self.findJetons()
            n = Noeud(antecedent)
            for place in marquage:
                n.addValue(place._nom, place._jetons)

            # ajoute le nouveau noeud à l'arbre
            if not self._graph.addNoeud(n, t) and not self._graph.isGenerator(n, t):
                # recursivite si pas d'antecedent pareil
                self.parcoursGraph(n, nb+1)

            t.inverserTransition()
    
    def printGraph(self):
        print("Graph:", self._graph._nom)
        self._graph.printGraph()



    def IsReseauBorne(self):
        return self._arbre._isBorne

    def estbloquant(self):
        # teste si un reseau est bloquant
        return (self._bloquant, self._marquageBloque)
    
    def estQuasiVivant(self):
        # teste si un reseau est quasi vivant
        for t in self._listTransitions:
            if t not in self._transitionsParcourues:
                return (False, t._nom)
        return (True, None)
    
    def estPropre(self):
        # si y'a pas le M0 dans l'arbre (hors premier noud) 
        if self._transitionsParcourues[0] in self._transitionsParcourues[0:]:
            return False
        # si c'est bloquant
        if self.estbloquant():
            return False
