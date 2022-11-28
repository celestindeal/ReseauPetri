
class Noeud():
    """
    noeud d'un arbre
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
        compare si ce neoud a la meme valeur que le noeud en paramètre, cad qu'il a les memes places avec le meme nombre de jetons
        """
        for key in self._valeurs:
            # si la place n'est pas dans les places de l'autre noeud
            if key not in noeud._valeurs:
                return False
            else:
                # si les deux places existent, on vérifie qu'il y a ait le meme nombre de jetons
                if self._valeurs[key] != noeud._valeurs[key]:
                    return False

        # si des places existent dans noeud mais pas dans self -> false
        for key in noeud._valeurs:
            if key not in self._valeurs:
                return False

        return True
