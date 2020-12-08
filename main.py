from classes import *


p1 = Prof(True, 'nomp1', 'prenomp1')
e1 = Lyceen( 'nome1', 'prenome1')
e2 = Lyceen( 'nome2', 'prenome2')
e3 = Lyceen( 'nome3', 'prenome3')

classe1 = Classe(10, 'classe1')
classe1.add_lyceen(e1)
classe1.add_lyceen(e2)
classe1.add_lyceen(e3)

bus1 = Bus()
bus1.add_passager(p1)
bus1.add_passager(e1)
bus1.add_passager(e2)
bus1.add_passager(e3)

print(bus1.getNbPlacesMax())

bus1.faireAppel()

if bus1.peutPartir():
    bus1.partir("Choucroutte")
