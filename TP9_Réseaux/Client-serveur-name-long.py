from reseauPetri.perti import Petri
from reseauPetri.place import Place


''' Réseau Client Serveur '''


ClientServeur = Petri('TD R1')


# Place de l'état du client 
clientDeco = Place("clientDeco",1)
clientAttConnexion = Place("clientAttConnexion",0)
clientCo = Place("clientCo",0)
clientAttDeco = Place("clientAttDeco",0)

# Place de l'état du serveur
ServeurDeco = Place("ServeurDeco",1)
ServeurCo = Place("ServeurCo",0)
ServeurAttDeco = Place("ServeurAttDeco",0)


# Place des l'états de transition 
DemandeConnexionClient = Place("DemandeConnexionClient",0)
ComfirmationConnexionServeur = Place("ComfirmationConnexionServeur",0)
DemandeDeconnexionServeur = Place("DemandeDeconnexionServeur",0)                # le serveur demande la déconnexion
ComfirmationDeconnexionCLient = Place("ComfirmationDeconnexionClient",0)
DemandeDeconnexionClient = Place("DemandeDeconnexionClient",0)                  # le client demande la déconnexion
ComfirmationDeconnexionServeur = Place("ComfirmationDeconnexionServeur",0)


# Ajouter les places et les transitions au réseau

ClientServeur.addPlace(clientDeco)
ClientServeur.addPlace(clientAttConnexion)
ClientServeur.addPlace(clientCo)
ClientServeur.addPlace(clientAttDeco)
ClientServeur.addPlace(ServeurDeco)
ClientServeur.addPlace(ServeurCo)
ClientServeur.addPlace(ServeurAttDeco)
ClientServeur.addPlace(DemandeConnexionClient)
ClientServeur.addPlace(ComfirmationConnexionServeur)
ClientServeur.addPlace(DemandeDeconnexionServeur)
ClientServeur.addPlace(ComfirmationDeconnexionCLient)
ClientServeur.addPlace(DemandeDeconnexionClient)
ClientServeur.addPlace(ComfirmationDeconnexionServeur)


ClientServeur.addTransition('A', {clientDeco:1}, {clientAttConnexion:1,DemandeConnexionClient:1})
ClientServeur.addTransition('B', {clientAttConnexion:1,ComfirmationConnexionServeur:1}, {clientCo:1})
ClientServeur.addTransition('E', {clientCo:1,DemandeDeconnexionServeur:1}, {clientDeco:1,ComfirmationDeconnexionCLient:1})
ClientServeur.addTransition('C', {clientCo:1}, {clientAttDeco:1,DemandeDeconnexionClient:1})                     # le client demande la déconnexion
ClientServeur.addTransition('D', {clientAttDeco:1,ComfirmationDeconnexionServeur:1}, {clientDeco:1})
ClientServeur.addTransition('F', {DemandeConnexionClient:1,ServeurDeco:1}, {ComfirmationConnexionServeur:1,ServeurCo:1})
ClientServeur.addTransition('G', {ServeurCo:1}, {ServeurAttDeco:1,DemandeDeconnexionServeur:1})                     # le serveur demande la déconnexion
ClientServeur.addTransition('H', {ServeurAttDeco:1,ComfirmationDeconnexionCLient:1}, {ServeurDeco:1})
ClientServeur.addTransition('I', {DemandeDeconnexionClient:1,ServeurCo:1}, {ServeurDeco:1,ComfirmationDeconnexionServeur:1})
# COMMENTEZ CETTE LIGNE POUR RENDRE LE RÉSEAU BLOQUANT LORSQUE LE CLIENT ET LE SERVEUR DEMANDENT LA DECONNEXION EN MEME TEMPS
ClientServeur.addTransition('J', {clientAttDeco:1,ServeurAttDeco:1,DemandeDeconnexionClient:1,DemandeDeconnexionServeur:1}, {ServeurDeco:1,clientDeco:1})


ClientServeur.buildArbre()
ClientServeur.printArbre()
ClientServeur.buildGraph()
ClientServeur.printGraph()
ClientServeur._graph.printVE()
print("Le réseau est-il borné ? ->", ClientServeur.IsReseauBorne())
print("Le réseau est-il bloquant ? ->", ClientServeur.estbloquant())
print("Le réseau est-il quasi vivant ? ->", ClientServeur.estQuasiVivant())
print("Vous pouvez commenter la ligne 58 pour supprimer la transition J et rendre le\
 réseau bloquant si le client et le serveur demandent la déconnexion en même temps.")

