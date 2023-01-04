from reseauPetri.perti import Petri
from reseauPetri.place import Place


''' Réseau Client Serveur '''


ClientServeur = Petri('TD R1')


# Place de l'état du client 
clientDeco = Place("1",1, [], [])
clientAttConnexion = Place("2",0,[],[])
clientCo = Place("3",0,[],[])
clientAttDeco = Place("4",0,[],[])

# Place de l'état du serveur
ServeurDeco = Place("5",1, [], [])
ServeurCo = Place("6",0,[],[])
ServeurAttDeco = Place("7",0,[],[])


# Place des l'états de transition 
DemandeConnexionClient = Place("8",0, [], [])
ComfirmationConnexionServeur = Place("9",0,[],[])
DemandeDeconnexionServeur = Place("10",0,[],[])                # le serveur demande la déconnexion
ComfirmationDeconnexionCLient = Place("11",0,[],[])
DemandeDeconnexionClient = Place("12",0,[],[])                  # le client demande la déconnexion
ComfirmationDeconnexionServeur = Place("13",0,[],[])


# déclaration des places suivantes
#


clientDeco.addPlaceSuivant([clientAttConnexion,DemandeConnexionClient,DemandeDeconnexionServeur,clientAttDeco,DemandeDeconnexionClient,ServeurAttDeco])
clientAttConnexion.addPlaceSuivant([clientCo,clientDeco,ServeurDeco])
clientCo.addPlaceSuivant([clientAttDeco,DemandeDeconnexionClient,ComfirmationDeconnexionCLient])
clientAttDeco.addPlaceSuivant([clientDeco,ServeurDeco])

ServeurDeco.addPlaceSuivant([ServeurCo,ComfirmationConnexionServeur,DemandeDeconnexionServeur,clientAttDeco,DemandeDeconnexionClient,ServeurAttDeco])
ServeurCo.addPlaceSuivant([ServeurAttDeco,ComfirmationDeconnexionServeur,ServeurDeco])
ServeurAttDeco.addPlaceSuivant([clientDeco,ServeurDeco,clientDeco])

DemandeConnexionClient.addPlaceSuivant([ServeurCo,ComfirmationConnexionServeur])
ComfirmationConnexionServeur.addPlaceSuivant([clientCo])
DemandeDeconnexionServeur.addPlaceSuivant([ComfirmationDeconnexionCLient,clientDeco,ServeurDeco,clientDeco])
ComfirmationDeconnexionCLient.addPlaceSuivant([ServeurDeco])
DemandeDeconnexionClient.addPlaceSuivant([ComfirmationDeconnexionServeur,clientDeco,ServeurDeco])
ComfirmationDeconnexionServeur.addPlaceSuivant([clientDeco])



#  Déclaration des antécédents

clientDeco.addPlaceAntecedant([clientCo,DemandeDeconnexionServeur,clientAttDeco,ComfirmationDeconnexionServeur])
clientAttConnexion.addPlaceAntecedant([clientDeco,DemandeConnexionClient])
clientCo.addPlaceAntecedant([clientAttConnexion,ComfirmationConnexionServeur])
clientAttDeco.addPlaceAntecedant([clientCo])

ServeurDeco.addPlaceAntecedant([ServeurCo,DemandeDeconnexionClient,ServeurAttDeco,ComfirmationDeconnexionCLient])
ServeurCo.addPlaceAntecedant([ServeurDeco,DemandeConnexionClient])
ServeurAttDeco.addPlaceAntecedant([ServeurCo])

DemandeConnexionClient.addPlaceAntecedant([clientDeco])
ComfirmationConnexionServeur.addPlaceAntecedant([DemandeConnexionClient,ServeurDeco])
DemandeDeconnexionServeur.addPlaceAntecedant([ServeurCo])
ComfirmationDeconnexionCLient.addPlaceAntecedant([DemandeDeconnexionServeur,clientCo])
DemandeDeconnexionClient.addPlaceAntecedant([clientCo])
ComfirmationDeconnexionServeur.addPlaceAntecedant([ServeurCo,DemandeDeconnexionClient])

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
ClientServeur.addTransition('B',  {clientAttConnexion:1,ComfirmationConnexionServeur:1}, {clientCo:1})
ClientServeur.addTransition('E', {clientCo:1,DemandeDeconnexionServeur:1}, {clientDeco:1,ComfirmationDeconnexionCLient:1})
ClientServeur.addTransition('C', {clientCo:1}, {clientAttDeco:1,DemandeDeconnexionClient:1})                     # le client demande la déconnexion
ClientServeur.addTransition('D', {clientAttDeco:1,ComfirmationDeconnexionServeur:1}, {clientDeco:1})
ClientServeur.addTransition('F', {DemandeConnexionClient:1,ServeurDeco:1}, {ComfirmationConnexionServeur:1,ServeurCo:1})
ClientServeur.addTransition('G', {ServeurCo:1}, {ServeurAttDeco:1,DemandeDeconnexionServeur:1})                     # le serveur demande la déconnexion
ClientServeur.addTransition('H', {ServeurAttDeco:1,ComfirmationDeconnexionCLient:1}, {ServeurDeco:1})
ClientServeur.addTransition('I', {DemandeDeconnexionClient:1,ServeurCo:1}, {ServeurDeco:1,ComfirmationDeconnexionServeur:1})
# COMMENTEZ CETTE LIGNE POUR RENDRE LE RÉSEAU BLOQUANT LORSQUE LE CLIENT ET LE SERVEUR DEMANDENT LA DECONNEXION EN MEME TEMPS
ClientServeur.addTransition('J', {clientAttDeco:1,ServeurAttDeco:1,DemandeDeconnexionClient:1,DemandeDeconnexionServeur:1}, {ServeurDeco:1,clientDeco:1})
# R1.printreseauPetri()


#KarpMiller(petri)


ClientServeur.buildArbre()
ClientServeur.printArbre()
ClientServeur.buildGraph()
ClientServeur.printGraph()
ClientServeur._graph.printVE()
print("Le réseau est-il borné ? ->", ClientServeur.IsReseauBorne())
print("Le réseau est-il blaquant ? ->", ClientServeur.estbloquant())
print("Le réseau est-il quasi vivant ? ->", ClientServeur.estQuasiVivant())
print("Vous pouvez commenter la ligne 99 pour supprimer la transition J et rendre le\
 réseau bloquant si le client et le serveur demandent la déconnexion en même temps.")

