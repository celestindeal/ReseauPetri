
class Transition():
    """
    transition entre plusieurs places sur un réseau de pétri, représentée par un ⬜
    """

    def __init__(self, nom, condition, action) -> None:
        """
        constructeur
        :param nom: nom de la transition
        :param conditions: conditions pour pouvoir executer la transition. Dictionnaire ayant pour clé la liste
                           des places depuis lesquelles prendre un/des jeton.s et ayant pour valeur le nombre
                           de jetons à prendre
        :param action: action à réaliser après la transition. Dictionnaire ayant pour clé la liste
                           des places vers lesquelles donner un/des jeton.s et ayant pour valeur le nombre
                           de jetons à donner
        """
        self._nom = nom                 # nom de la transition
        self._conditions = condition    # place : nombre de jetons à prendre
        self._actions = action          # place : nombre de jetons à donner

    def addCondition(self, place, jetons):
        self._conditions[place] = jetons

    def addAction(self, place, jetons):
        self._actions[place] = jetons

    def execTransition(self):
        """
        exectute la transition. Ne vérifie pas si la transition est possible.
        retire le nombre de jetons nécéssaires aux places de condition et donne le nombre de
        jetons nécessaires aux places d'action
        """
        for key in self._conditions:
            key._jetons -= self._conditions[key]
        for key in self._actions:
            key._jetons += self._actions[key]
    
    def inverserTransition(self):
        for key in self._conditions:
            key._jetons += self._conditions[key]
        for key in self._actions:
            key._jetons -= self._actions[key]


