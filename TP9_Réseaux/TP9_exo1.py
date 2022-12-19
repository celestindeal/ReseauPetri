from reseauPetri.perti import Petri
from reseauPetri.place import Place


# réalisation de l'algo Karp-Miller


''' Test de l'algo Karp-Miller '''


R1 = Petri('TD R1')


# Create reseauPetri 
place1 = Place("1",1, [], [])
place2 = Place("2",0,[place1],[])
place3 = Place("3",0,[place1],[])
place4 = Place("4",0,[place2],[])
place5 = Place("5",0,[place4],[])
place1.addPlaceAntecedant([place4,place5])
place1.addPlaceSuivant([place2,place3])
R1.addPlace(place1)
R1.addPlace(place2)
R1.addPlace(place3)
R1.addPlace(place4)
R1.addPlace(place5)
R1.addTransition('A', {place1:1}, {place2:1,place3:1})
R1.addTransition('B', {place2:1}, {place4:1})
R1.addTransition('C', {place3:1}, {place5:1})
R1.addTransition('D', {place5:1}, {place3:1})
R1.addTransition('E', {place4:1,place5:1}, {place1:1})
# R1.printreseauPetri()


#KarpMiller(petri)

R1.buildArbre()
R1.printArbre()
# print("Le réseau est-il borné ? ->", R1.IsReseauBorne())


'''Test réseau de Petri Générateur'''

R5 = Petri('TD R5')
place1Generator = Place("1",1, [], [])
place1Generator.addPlaceAntecedant([place1Generator])
place2Generator = Place("2",0,[place1Generator],[])
R5.addPlace(place1Generator)
R5.addPlace(place2Generator)
R5.addTransition('A', {place1Generator:1}, {place1Generator:1,place2Generator:1})
R5.addTransition('B', {place1Generator:1}, {})

#KarpMiller(petri)
R5.buildArbre()


# R5.printreseauPetri()
R5.printArbre()
# print("Le réseau est-il borné ? ->", R5.IsReseauBorne())