import requests
import sys
from classes import *
from interface import *
from PyQt5.QtWidgets import QApplication


### On lance l'interface visuelle

app = QApplication(sys.argv)
ex = Interface()
sys.exit(app.exec_())


p1 = Prof(True, 'nomp1', 'prenomp1')
p2 = Prof(False, 'nomp2', 'prenomp2')
e1 = Lyceen( 'nome1', 'prenome1')
e2 = Lyceen( 'nome2', 'prenome2')
e3 = Lyceen( 'nome3', 'prenome3')
e4 = Lyceen( 'nome4', 'prenome4')
e5 = Lyceen( 'nome5', 'prenome5')
e6 = Lyceen( 'nome6', 'prenome6')
e7 = Lyceen( 'nome7', 'prenome7')
e8 = Lyceen( 'nome8', 'prenome8')
e9 = Lyceen( 'nome9', 'prenome9')
e10 = Lyceen( 'nome10', 'prenome10')
e11 = Lyceen( 'nome11', 'prenome11')

classe1 = Classe(10, 'classe1')
classe2 = Classe(10, 'classe2')
classe3 = Classe(10, 'classe3')
classe4 = Classe(10, 'classe4')
classe1.add_lyceen(e1)
classe2.add_lyceen(e2)
classe2.add_lyceen(e3)
classe3.add_lyceen(e4)
classe1.add_lyceen(e5)
classe1.add_lyceen(e6)
classe1.add_lyceen(e7)
classe1.add_lyceen(e8)
classe1.add_lyceen(e9)
classe1.add_lyceen(e10)
classe1.add_lyceen(e11)

bus1 = Bus()
bus1.add_passager(p1)
bus1.add_passager(p2)
bus1.add_passager(e1)
bus1.add_passager(e2)
bus1.add_passager(e3)
bus1.add_passager(e4)
bus1.add_passager(e5)
bus1.add_passager(e6)
bus1.add_passager(e7)
bus1.add_passager(e8)
bus1.add_passager(e9)
bus1.add_passager(e10)
bus1.add_passager(e11)

print(bus1.getNbPlacesMax())
print(classe1.listLyceen)
bus1.faireAppel()

if bus1.peutPartir():
    bus1.partir("Choucroutte")
