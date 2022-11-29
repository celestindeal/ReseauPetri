
from reseauPetri.perti import Petri
from reseauPetri.place import Place



# réalisation de l'algo Karp-Miller
def KarpMiller(petri):
    
    return 0



''' Test de l'algo Karp-Miller '''

petri = Petri('Karp and Miller')



# Create reseauPetri 
place1 = Place("1",1, [], [])
place2 = Place("2",0,[place1],[])
place3 = Place("3",0,[place1],[])
place4 = Place("4",0,[place2],[])
place5 = Place("5",0,[place4],[])
place1.addPlaceAntecedant([place4,place5])
place1.addPlaceSuivant([place2,place3])

petri.addPlace(place1)
petri.addPlace(place2)
petri.addPlace(place3)
petri.addPlace(place4)
petri.addPlace(place5)

petri.addTransition('A', {place1:1}, {place2:1,place3:1})
petri.addTransition('B', {place2:1}, {place4:1})
petri.addTransition('C', {place3:1}, {place5:1})
petri.addTransition('D', {place5:1}, {place3:1})
petri.addTransition('E', {place4:1,place5:1}, {place1:1})


petri.printreseauPetri()
#KarpMiller(petri)
petri.buildArbre()



'''Test réseau de Petri Générateur'''

petriGenerator = Petri('Generator')

place1Generator = Place("1",1, [], [])
place1Generator.addPlaceAntecedant([place1Generator])
place2Generator = Place("2",0,[place1Generator],[])

petriGenerator.addPlace(place1Generator)
petriGenerator.addPlace(place2Generator)
petriGenerator.addTransition('A', {place1Generator:1}, {place1Generator:1,place2Generator:1})
petriGenerator.addTransition('B', {place1Generator:1}, {})



petriGenerator.printreseauPetri()
#KarpMiller(petri)
petriGenerator.buildArbre()