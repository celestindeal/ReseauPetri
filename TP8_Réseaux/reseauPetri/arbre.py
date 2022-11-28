
class Arbre ():
    """
    Arbre des marquages d'un réseau de pétri
    """

    def __init__(self,nom) -> None:
        """
        constructeur
        """
        self._nom = nom         # nom de l'arbre (nom du réseau)
        self._listNoeud = []    # liste des noeuds

    def printArbre(self, texte=None, n=None):
        """
        affiche l'arbre
        """

        # TODO: oui je sais t'aime pas faut faire deux fonctions
        if n== None:
            n = self._listNoeud[0]
            texte = n.toString()

        # quand on arrive sur une feuille
        if n._enfants == {}:
            texte += "\n"
            return texte
        # sinon on ajoute la transistion et la valeur du noeud
        else:
            for key in n._enfants:
                texte += " -" + key + "-> " + n._enfants[key].toString()
                texte = self.printArbre(texte, n._enfants[key])
        print(texte)
        return texte
    
    def toString(self):
        """
        liste des noeuds en string
        """
        texte = ""
        for noeud in self._listNoeud:
            texte += noeud.toString() + "\n"
        return texte


    def addNoeud(self, noeud, transition):
        """
        ajoute le neoud à l'arbre depuis la transition.
        si le neoud n'a pas de parent, on l'ajoute directement à l'arbre, sinon, on vérifie si ce noeud existe déjà parmis
        ses antécédents, puis on l'ajoute en tant qu'enfant de son parent et on l'ajoute à l'arbre
        :return: True si même antécédent trouvé, False sinon
        """
        check = False
        # pour les noeuds qui on un antécédents
        if noeud._parent != None:
            n = noeud
            # on parcours l'arbre 'à l'envers' -> on parcours les antécédents
            while n._parent != None:
                # on vérifie si le nouveau noeud existe déjà parmis les antécédents
                if noeud.compareNoeud(n._parent):
                    check = True
                n = n._parent
            # on ajoute ce noeud comme étant l'enfant de son parent
            noeud._parent.addEnfant(transition._nom, noeud)
        # on ajoute le noeud à l'arbre
        self._listNoeud.append(noeud)
        return check