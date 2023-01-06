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
R1.buildGraph()
R1._graph.printVE()
R1.printGraph()
print("Le réseau est-il borné ? ->", R1.IsReseauBorne())
print("Le réseau est-il bloquant ? ->", R1.estbloquant())
print("Le réseau est-il propre ? ->", R1.estPropre())
print("Le réseau est-il quasi vivant ? ->", R1.estQuasiVivant())


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
R5.buildGraph()
R5.printGraph()
R5._graph.printVE()
print("Le réseau est-il borné ? ->", R5.IsReseauBorne())
print("Le réseau est-il bloquant ? ->", R5.estbloquant())
print("Le réseau est-il propre ? ->", R5.estPropre())
print("Le réseau est-il quasi vivant ? ->", R5.estQuasiVivant())

## R2
R2 = Petri('TD R2')
R2place1 = Place("1",1, [], [])
R2place2 = Place("2",1, [R2place1], [])
R2place3 = Place("3",1, [], [])
R2place4 = Place("4",0, [R2place1, R2place2], [R2place1, R2place2])
R2place5 = Place("5",0, [R2place2, R2place3], [R2place3, R2place2])
R2place2.addPlaceAntecedant([R2place3, R2place4, R2place5])
R2place3.addPlaceAntecedant([R2place5])
R2place1.addPlaceAntecedant([R2place4])
R2place1.addPlaceSuivant([R2place4])
R2place2.addPlaceSuivant([R2place4, R2place5])
R2place3.addPlaceSuivant([R2place5])
R2.addPlace(R2place1)
R2.addPlace(R2place2)
R2.addPlace(R2place3)
R2.addPlace(R2place4)
R2.addPlace(R2place5)
R2.addTransition('A', {R2place1:1, R2place2:1}, {R2place4:1})
R2.addTransition('B', {R2place2:1, R2place3:1}, {R2place5:1})
R2.addTransition('C', {R2place4:1}, {R2place2:1, R2place1:1})
R2.addTransition('D', {R2place4:1, R2place5:1}, {})
R2.addTransition('E', {R2place5:1}, {R2place3:1, R2place2:1})

#KarpMiller(petri)
R2.buildArbre()


# R5.printreseauPetri()
R2.printArbre()
R2.buildGraph()
R2.printGraph()
R2._graph.printVE()
print("Le réseau est-il borné ? ->", R2.IsReseauBorne())
print("Le réseau est-il bloquant ? ->", R2.estbloquant())
print("Le réseau est-il propre ? ->", R2.estPropre())
print("Le réseau est-il quasi vivant ? ->", R2.estQuasiVivant())
