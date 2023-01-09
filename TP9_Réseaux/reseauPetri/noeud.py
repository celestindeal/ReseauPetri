
class Noeud():
    """
    noeud d'un arbre ou d'un graphe
    """

    def __init__(self, parent):
        """
        constructeur
        """
        self._valeurs = {}          # nom de la place : nombre de jetons
        self._parent = parent       # noeud parent
        self._enfants = {}          # neurds enfants -> clé = nom de la transition : valeur = neoud enfant
    
    def toString(self):
        """
        retourne la valeur du noeud en str
        """
        texte = ""
        if self._valeurs == {}:
            texte = "ø"
        else:
            for key in self._valeurs:
                texte += key \
                    + "^" \
                    + str(self._valeurs[key]) \
                    + " "
        return texte
    
    def addValue(self, nomPlace, nbJetons):
        """
        compose la valeur du noeud, l'état du marquage en ajoutant pour cette place son nombre de jetons
        """
        self._valeurs[nomPlace] = nbJetons
    
    def addEnfant(self, nomTransition, neudEnfant):
        self._enfants[nomTransition] = neudEnfant

    def compareNoeud(self, noeud):
        """
        compare si ce noeud a la même valeur que le noeud en paramètre, cad qu'il a les mêmes places avec le même nombre de jetons
        """
        for key in self._valeurs:
            # si la place n'est pas dans les places de l'autre noeud
            if key not in noeud._valeurs:
                return False
            else:
                # si les deux places existent, on vérifie qu'il y ait le même nombre de jetons
                if self._valeurs[key] != noeud._valeurs[key]:
                    return False

        # si des places existent dans noeud mais pas dans self -> false
        for key in noeud._valeurs:
            if key not in self._valeurs:
                return False

        return True
    
    def compareNoeudGenerator(self, noeudenfant):
        """
        pour chaque place dans le noeud, on contrôle que le noeud enfant a la même place et le même nombre de jetons ou plus 
        """

        #  problème il existe le cas où le parent a des places que l'enfant n'a pas
        for key in noeudenfant._valeurs:
            try:                    # si la place n'existe pas dans le noeud enfant
                if self._valeurs[key] > noeudenfant._valeurs[key]:
                    return False
            except KeyError:
                return False

        return True
