
class Arbre ():
    """
    Arbre des marquages d'un réseau de pétri
    """

    NB_PLACE_PAR_NOEUD = 3 # pour l'affichage

    def __init__(self,nom) -> None:
        """
        constructeur
        """
        self._nom = nom         # nom de l'arbre (nom du réseau)
        self._listNoeud = []    # liste des noeuds
        self._isBorne = True

    def printArbre(self):
        """
        affiche l'arbre
        """
        texte = self.parcoursPrintArbre(
            "      "                                    # nombre d'espaces dans une flèche
            + self._listNoeud[0].toString()             # valeur du premier noeud
                  .ljust(Arbre.NB_PLACE_PAR_NOEUD*4),   # ajoute le nombre d'espaces pour 3 noeuds
            self._listNoeud[0],           # le premier noeud
            1)
        
        print(texte)
    
      
      
    def parcoursPrintArbre(self, texte, n, niveau):
        """
        fonction récursive pour afficher l'arbre
        """

        def hasAntecedent(n):
            antecedent = []  # liste des antecedents
            antecedent.append(n._parent)    # on ajoute le premier antecedent
            if n._parent == None:  # si il n'y a pas d'antecedent 
                return 0
            else:
                while antecedent != [None] :    # tant qu'il y a des antecedents
                    if  n.compareNoeud(antecedent[0]):   
                    # if value == antecedent[0]._valeurs:   
                        return 1
                    elif n.compareNoeudGenerator(antecedent[0]):
                        return 2
                    antecedent.append(antecedent[0]._parent)   # on ajoute les autres antecedents
                    del (antecedent[0])   # on supprime le premier antecedent étudié pour passer au suivant
            return 0


        # quand on arrive sur une feuille
        if n._enfants == {}:
            texte += "\n"
            return texte
        # sinon
        else:
            # on parcours les enfants
            for key in n._enfants:
                # ajoute le bon nombre d'espaces
                if texte[-1] == '\n':
                    nb_espace = (6 + Arbre.NB_PLACE_PAR_NOEUD*4) * niveau
                    texte += "".ljust(nb_espace)
                # ajoute au texte le nom de la transition et la valeur du noeud : -t-> noeud
                
                boucle = hasAntecedent(n._enfants[key])
                if boucle == 1:  # si le noeud a un antécédent
                    texte +=  key + "-> " + n._enfants[key].toString() + "(Valeur déjà rencontrée)" 
                elif boucle == 2:  # si le noeud est un noeud de génération 
                    texte += " noeud de génération"+ " (" + key + "-> " + n._enfants[key].toString() + ")" 
                else:
                    texte += " -" + key + "-> " + n._enfants[key].toString().ljust(Arbre.NB_PLACE_PAR_NOEUD*4)
                # recursivité : parcours des enfants
                texte = self.parcoursPrintArbre(texte, n._enfants[key], niveau+1)
        return texte   

  
    
    def toString(self):
        """
        liste des noeuds en string
        """
        texte = ""
        for noeud in self._listNoeud:
            texte += noeud.toString() + "\n"
        return texte

    def isGenerator(self, noeud, transition):
        """
        vérifie si une transition 'génère' des jetons, cad que pour les mêmes places à l'antécédent le nb de jetons augmente
        """
        
        if noeud._parent != None:
            n = noeud
            # on parcourt l'arbre 'à l'envers' -> on parcourt les antécédents
            while n._parent != None:
                # on vérifie si le nouveau noeud existe déjà parmi les antécédents
                if noeud.compareNoeudGenerator(n._parent):
                    self._isBorne = False
                    return True
                n = n._parent
        return False

    def addNoeud(self, noeud, transition):
        """
        ajoute le neoud à l'arbre depuis la transition.
        si le neoud n'a pas de parent, on l'ajoute directement à l'arbre, sinon, on vérifie si ce noeud existe déjà parmi
        ses antécédents, puis on l'ajoute en tant qu'enfant de son parent et on l'ajoute à l'arbre
        :return: True si même antécédent trouvé, False sinon
        """
        check = False
        # pour les noeuds qui ont un antécédents
        if noeud._parent != None:
            n = noeud
            # on parcourt l'arbre 'à l'envers' -> on parcourt les antécédents
            while n._parent != None:
                # on vérifie si le nouveau noeud existe déjà parmi les antécédents
                if noeud.compareNoeud(n._parent):
                    check = True
                n = n._parent
            # on ajoute ce noeud comme étant l'enfant de son parent
            noeud._parent.addEnfant(transition._nom, noeud)
        # on ajoute le noeud à l'arbre
        self._listNoeud.append(noeud)
        return check

