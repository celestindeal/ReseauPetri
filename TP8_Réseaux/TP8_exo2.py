from reseauPetri.perti import Petri
from reseauPetri.place import Place


# réalisation de l'algo Karp-Miller



''' Traverser la rivière '''


petri = Petri('Traverser la rivière')


### A met 10mn
### B met 5mn
### C met 2mn
### D met 1mn

# Create reseauPetri 
placeAd = Place("A départ",1, [], [])
placeBd = Place("B départ",1, [], [])
placeCd = Place("C départ",1, [], [])
placeDd = Place("D départ",1, [], [])
placeLd = Place("L départ",1, [], [])
placeAa = Place("A arrivée",0, [placeAd], [])
placeBa = Place("B arrivée",0, [placeBd], [])
placeCa = Place("C arrivée",0, [placeCd], [])
placeDa = Place("D arrivée",0, [placeDd], [])
placeLa = Place("L arrivée",0, [placeLd], [])

placeTemps = Place("Temps",0, [], [])


placeAd.addPlaceSuivant([placeAa])
placeBd.addPlaceSuivant([placeBa])
placeCd.addPlaceSuivant([placeCa])
placeDd.addPlaceSuivant([placeDa])
placeLd.addPlaceSuivant([placeLa])

petri.addPlace(placeAd)
petri.addPlace(placeBd)
petri.addPlace(placeCd)
petri.addPlace(placeDd)
petri.addPlace(placeLd)
petri.addPlace(placeAa)
petri.addPlace(placeBa)
petri.addPlace(placeCa)
petri.addPlace(placeDa)
petri.addPlace(placeLa)
petri.addPlace(placeTemps)

petri.addTransition('ABa', {placeAd:1, placeBd:1, placeLd:1}, {placeAa:1, placeBa:1, placeLa:1, placeTemps:10})
petri.addTransition('ACa', {placeAd:1, placeCd:1, placeLd:1}, {placeAa:1, placeCa:1, placeLa:1, placeTemps:10})
petri.addTransition('ADa', {placeAd:1, placeDd:1, placeLd:1}, {placeAa:1, placeDa:1, placeLa:1, placeTemps:10})
petri.addTransition('BCa', {placeBd:1, placeCd:1, placeLd:1}, {placeBa:1, placeCa:1, placeLa:1, placeTemps:5})
petri.addTransition('BDa', {placeBd:1, placeDd:1, placeLd:1}, {placeBa:1, placeDa:1, placeLa:1, placeTemps:5})
petri.addTransition('CDa', {placeCd:1, placeBd:1, placeLd:1}, {placeCa:1, placeDa:1, placeLa:1, placeTemps:2})

petri.addTransition('Ar', {placeAa:1, placeLa:1}, {placeAd:1, placeLd:1, placeTemps:10})
petri.addTransition('Br', {placeBa:1, placeLa:1}, {placeBd:1, placeLd:1, placeTemps:5})
petri.addTransition('Cr', {placeCa:1, placeLa:1}, {placeCd:1, placeLd:1, placeTemps:2})
petri.addTransition('Dr', {placeDa:1, placeLa:1}, {placeDd:1, placeLd:1, placeTemps:1})
petri.printreseauPetri()



#KarpMiller(petri)

petri.buildArbre()

print("Le réseau est-il borné ? ->", petri.IsReseauBorne())


