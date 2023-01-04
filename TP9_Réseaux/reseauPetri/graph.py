from.arc import Arc

class Graph ():
    """
    Graph des marquages d'un réseau de pétri
    """

    NB_PLACE_PAR_NOEUD = 3

    def __init__(self,nom) -> None:
        """
        constructeur
        """
        self._nom = nom         # nom de l'Graph (nom du réseau)
        self._listNoeud = []    # liste des noeuds
        self._isBorne = True
        self._listArcs = []

    def printGraph(self):
        """
        affiche l'Graph
        """
        texte = self.parcoursPrintGraph(
            "      "                                    # nombre d'espaces dans une flèche
            + self._listNoeud[0].toString()             # valeur du premier noeud
                  .ljust(Graph.NB_PLACE_PAR_NOEUD*4),   # ajoute le nombre d'espaces pour 3 noeuds
            self._listNoeud[0],                         # le premier noeud
            1,                                          # le niveau
            []                                          # les noeuds parcourus
        )
        
        print(texte)
    
      
      
    def parcoursPrintGraph(self, texte, n, niveau, parcourus):

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
                    nb_espace = (6 + Graph.NB_PLACE_PAR_NOEUD*4) * niveau
                    texte += "".ljust(nb_espace)
                # ajoute au texte le nom de la transition et la valeur du noeud : -t-> noeud
                
                if n._enfants[key] in parcourus:  # si le noeud as un antécédent
                    texte += "On reboucle "+ " (" + key + "-> " + n._enfants[key].toString() + ")" 
                elif n._parent != None and n._parent.compareNoeudGenerator(n):  # si le noeud est un noeud de génération 
                    texte += " noeud de génération"+ " (" + key + "-> " + n._enfants[key].toString() + ")" 
                else:
                    texte += " -" + key + "-> " + n._enfants[key].toString().ljust(Graph.NB_PLACE_PAR_NOEUD*4)
                # recursivité : parcours des enfants
                if n._enfants[key] not in parcourus:
                    parcourus.append(n._enfants[key])
                    texte = self.parcoursPrintGraph(texte, n._enfants[key], niveau+1, parcourus)
                else:
                    # quand on arrive sur une feuille
                    texte += "\n"
                    
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
        
        if noeud._parent != None:
            n = noeud
            # on parcours l'Graph 'à l'envers' -> on parcours les antécédents
            while n._parent != None:
                # on vérifie si le nouveau noeud existe déjà parmis les antécédents
                if noeud.compareNoeudGenerator(n._parent):
                    self._isBorne = False
                    return True
                n = n._parent
        return False

    def addNoeud(self, noeud, transition):
        """
        ajoute le neoud à l'Graph depuis la transition.
        si le neoud n'a pas de parent, on l'ajoute directement à l'Graph, sinon, on vérifie si ce noeud existe déjà parmis
        ses antécédents, puis on l'ajoute en tant qu'enfant de son parent et on l'ajoute à l'Graph
        :return: True si même antécédent trouvé, False sinon
        """
        check = False
        # pour les noeuds qui on un antécédents
        if noeud._parent != None:
            n = noeud
            # si un antécédent avec les mêmes valeurs existe, il sera stocké dans cette variable
            ant = None
            # on parcours l'Graph 'à l'envers' -> on parcours les antécédents
            while n._parent != None:
                # on vérifie si le nouveau noeud existe déjà parmis les antécédents
                if noeud.compareNoeud(n._parent):
                    check = True
                    # on stocke le parent avec les mêmes valeurs
                    ant = n._parent
                n = n._parent
            # si un parent aux meme valeurs existe
            if check:
                # on ajoute ce parent comme étant l'enfant
                noeud._parent.addEnfant(transition._nom, ant)
                self._listArcs.append(Arc(noeud._parent, ant, transition._nom))
            # sinon
            else:
                # on ajoute ce noeud comme étant l'enfant de son parent
                noeud._parent.addEnfant(transition._nom, noeud)
                self._listArcs.append(Arc(noeud._parent, noeud, transition._nom))
                # on ajoute le noeud à l'arbre
                self._listNoeud.append(noeud)
        return check
    
    def printVE(self):
        print("V:")
        for n in self._listNoeud:
            print(n.toString())
        print("E:")
        for a in self._listArcs:
            print(a.toString())

