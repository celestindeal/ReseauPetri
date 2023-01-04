from reseauPetri.perti import Petri
from reseauPetri.place import Place


''' Réseau Client Serveur '''


ClientServeur = Petri('TD R1')


# Place de l'état du client 
clientDeco = Place("CDéco",1, [], [])
clientAttConnexion = Place("Catt",0,[],[])
clientCo = Place("Cco",0,[],[])
clientAttDeco = Place("CattDeco",0,[],[])

# Place de l'état du serveur
ServeurDeco = Place("SDéco",1, [], [])
ServeurCo = Place("Sco",0,[],[])
ServeurAttDeco = Place("SattDéco",0,[],[])


# Place des l'états de transition 
DemandeConnexionClient = Place("DC",0, [], [])
ComfirmationConnexionServeur = Place("CC",0,[],[])
DemandeDeconnexionServeur = Place("DDS",0,[],[])                # le serveur demande la déconnexion
ComfirmationDeconnexionCLient = Place("CDC",0,[],[])
DemandeDeconnexionClient = Place("DDC",0,[],[])                  # le client demande la déconnexion
ComfirmationDeconnexionServeur = Place("CDS",0,[],[])


# déclaration des places suivantes
#


clientDeco.addPlaceSuivant([clientAttConnexion,DemandeConnexionClient,DemandeDeconnexionServeur,clientAttDeco,DemandeDeconnexionClient,ServeurAttDeco])
clientAttConnexion.addPlaceSuivant([clientCo])
clientCo.addPlaceSuivant([clientAttDeco,DemandeDeconnexionClient,ComfirmationDeconnexionCLient])
clientAttDeco.addPlaceSuivant([clientDeco,ServeurDeco])

ServeurDeco.addPlaceSuivant([ServeurCo,ComfirmationConnexionServeur,DemandeDeconnexionServeur,clientAttDeco,DemandeDeconnexionClient,ServeurAttDeco])
ServeurCo.addPlaceSuivant([ServeurAttDeco,ComfirmationDeconnexionServeur,ServeurDeco])
ServeurAttDeco.addPlaceSuivant([clientDeco,ServeurDeco])

DemandeConnexionClient.addPlaceSuivant([ServeurCo,ComfirmationConnexionServeur])
ComfirmationConnexionServeur.addPlaceSuivant([clientCo])
DemandeDeconnexionServeur.addPlaceSuivant([ComfirmationDeconnexionCLient,clientDeco,ServeurDeco])
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
ClientServeur.addTransition('C', {clientCo:1,DemandeDeconnexionServeur:1}, {ComfirmationDeconnexionCLient:1})
ClientServeur.addTransition('D', {clientCo:1}, {clientAttDeco:1,DemandeDeconnexionClient:1})                     # le client demande la déconnexion
ClientServeur.addTransition('E', {clientAttDeco:1,ComfirmationDeconnexionServeur:1}, {clientDeco:1})
ClientServeur.addTransition('F', {DemandeConnexionClient:1,ServeurDeco:1}, {ComfirmationConnexionServeur:1,ServeurCo:1})
ClientServeur.addTransition('G', {ServeurCo:1}, {ServeurAttDeco:1,DemandeDeconnexionServeur:1})                     # le serveur demande la déconnexion
ClientServeur.addTransition('H', {ServeurAttDeco:1,ComfirmationDeconnexionCLient:1}, {ServeurDeco:1})
ClientServeur.addTransition('I', {DemandeDeconnexionClient:1,ServeurCo:1}, {ServeurDeco:1,ComfirmationDeconnexionServeur:1})
ClientServeur.addTransition('J', {clientAttConnexion:1,ServeurAttDeco:1,DemandeDeconnexionClient:1,DemandeDeconnexionServeur:1}, {ServeurDeco:1,clientCo:1})
# R1.printreseauPetri()


#KarpMiller(petri)


ClientServeur.buildArbre()
ClientServeur.printArbre()
ClientServeur.buildGraph()
ClientServeur.printGraph()
print("Le réseau est-il borné ? ->", ClientServeur.IsReseauBorne())
print("Le réseau est-il blaquant ? ->", ClientServeur.estbloquant())
print("Le réseau est-il quasi vivant ? ->", ClientServeur.estQuasiVivant())

