import requests
import sys
from classes import *
from interface import *
from PyQt5.QtWidgets import QApplication

print("Veuillez choisir la version à utilisé :")
choix = int(input("1 : Interface | 2 : Console \n"))

if choix == 1 :

    ### On lance l'interface visuelle

    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())

if choix == 2 :

    listeClasse = []
    listeEleve = []
    listeProf = []
    listeBus = []

    p1 = Prof(True, 'nomp1', 'prenomp1')
    p2 = Prof(False, 'nomp2', 'prenomp2')
    e1 = Lyceen('nome1', 'prenome1')
    e2 = Lyceen('nome2', 'prenome2')
    e3 = Lyceen('nome3', 'prenome3')
    e4 = Lyceen('nome4', 'prenome4')
    e5 = Lyceen('nome5', 'prenome5')
    e6 = Lyceen('nome6', 'prenome6')
    e7 = Lyceen('nome7', 'prenome7')
    e8 = Lyceen('nome8', 'prenome8')
    e9 = Lyceen('nome9', 'prenome9')
    e10 = Lyceen('nome10', 'prenome10')
    e11 = Lyceen('nome11', 'prenome11')

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

    bus1 = Bus("bus1")
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

    listeBus.append(bus1)

    ### On lance la boucle de la version console
    finGenerale = False
    Tour = 0
    while not finGenerale:
        print("\nVeuillez choisir ce que vous voulez faire:\n")
        choix = int(input("1 : Gestions des entitées \n2 : Gestion du départ des bus \n3 : Quitter\n"))

        if choix == 1:
            print("\nVeuillez choisir une action:\n")
            choixActionEntite = int(input("1 : Saisir de nouveaux passagers \n2 : Saisir de nouveaux bus \n3 : Saisir une nouvelle classe \n4: Afficher la listes des entités\n"))

            if choixActionEntite == 1:
                #Passagers
                print("Quel est le passager ?")
                choixPassagers = int(input("1 : Elève | 2 : Professeur \n"))

                if choixPassagers == 1 :
                    #Elève
                    print("Dans quelle classe ?")
                    classeEleve = input("Nom de la classe : ")
                    for classe in listeClasse :
                        if (classe.getNom() == classeEleve) :
                            eleveNom = str(input("Nom de l'élève : "))
                            elevePrenom = str(input("Prenom de l'élève : "))
                            listeEleve.append(Lyceen( eleveNom, elevePrenom))
                            for eleve in listeEleve :
                                if (eleve.getNom() == eleveNom and eleve.getPrenom() == elevePrenom) :
                                    classe.add_lyceen(eleve)

                if choixPassagers == 2 :
                    #Professeur
                    profNom = str(input("Nom du professeur : "))
                    profPrenom = str(input("Prenom du professeur : "))
                    profReferent = input("Référents ? (True/False)")
                    listeProf.append(Prof(profReferent, profNom, profPrenom))

            elif choixActionEntite == 2:
                #Bus
                busNom = str(input("Nom du bus : "))
                listeBus.append(Bus(busNom))
                
            elif choixActionEntite == 3:
                #Classe
                classeTaille = int(input("Taille de la classe : "))
                classeNom = str(input("Nom de la classe : "))
                listeClasse.append(Classe(classeTaille,classeNom))

            elif choixActionEntite == 4:
                #AfficherListes
                pass


        elif choix == 2:
            print("\nVeuillez choisir une action:\n")
            choixActionBus = int(input("1 : Afficher les bus et leurs passagers \n2 : Faire l'appel dans un bus \n3 : Faire partir un bus\n"))

            if choixActionBus == 1:
                #AfficherBusEtPassagers
                print("Ils y a actuellement "+str(len(listeBus))+" bus")
                for bus in listeBus:
                    print("\nLe bus "+bus.getNom()+" transporte "+str(len(bus.listPassager))+" passagers")
                    print("    Ces passagers sont: ")

                    listpassager = "        "
                    for passager in bus.listPassager:
                        listpassager += passager.getPrenom()+" "+passager.getNom()+"; "
                    print(listpassager[:-1])

            elif choixActionBus == 2:
                #Faireappel
                nomBus = input("Nom du bus: \n")
                for bus in listeBus:
                    if bus.getNom() == nomBus:
                        try:
                            bus.faireAppel()
                            print("Le bus peux partir : L'appel à été fait avec succès!")

                        except EleveAbsentException:
                            print("Le bus ne peux pas partir car il y a au moins un élève absent et/ou n'a pas de classe")



            elif choixActionBus == 3:
                #FairePartirBus
                nomBus = input("Nom du bus a faire partir: \n")
                for bus in listeBus:
                    if bus.getNom() == nomBus:
                        if bus.peutPartir():
                            bus.partir(nomBus)


        else:
            finGenerale = True








'''
        choix = int(input("1 : Saisir de nouveaux passagers \n2 : Saisir de nouveaux bus \n3 : Mettre des passagers dans un car \n4 : Afficher les bus \n5 : Faire partir les bus \n6 : Faire l'appel en tant que prof référent \n7 : Quitter \n8 : Gestion des classes \n"))
        
        if choix == 1 :
            #Saisir de nouveaux passagers
            print("Quel est le passager ?")
            choix = int(input("1 : Elève | 2 : Professeur \n"))

            if choix == 1 :
                #Elève
                listeEleve.append(Lyceen( input("Nom de l'élève : "), input("Prenom de l'élève : ")))

            if choix == 2 :
                #Professeur
                listeProf.append(Prof( input("Référents ? (True/False)"), input("Nom du professeur : "), input("Prenom du professeur : ")))

            finGenerale = False

        if choix == 2 :
            #Saisir de nouveaux bus
            #Besoin : Tous, les bus n'ont pas de nom pour les identifier
            print("Pas implémenter")
            #Nécessite d'ajouter un attribut nom aux bus
            finGenerale = False

        if choix == 3 :
            #Mettre des passagers dans un car
            #Besoin : Rajouter la condition de vérification des bus
            #         Géré les mauvaises saisies
            choixBus = input("Quel est le bus ? ")

            for bus in listeBus :
                #Nécessite de vérifier que le bus de la liste est celui choisi
                if (False) :
                    for passager in bus.listPassager :
                        choixPassager = input("Quel est le passager ? ")

                        if (passager.getNom == choixPassager) :
                            bus.add_passager(passager)

            finGenerale = False

        if choix == 4 :
            #Afficher les bus
            #Besoin : Ajouter le type de passager
            for bus in listeBus :
                for passager in bus.listPassager :
                    print("Nom : ", passager.getNom, " Prénom : ", passager.getPrenom)
                    #Nécessite de de rajouté le type de passager ?

            finGenerale = False

        if choix == 5 :
            #Faire partir les bus
            #Besoin : Rajouter la condition de vérification des bus
            #         Géré les mauvaises saisies
            #         Revoir l'exécution de la méthode "partir" de "bus"
            choixBus = input("Quel bus ? ")

            for bus in listeBus :
                #Nécessite de vérifier que le bus de la liste est celui choisi
                if (False) :
                    if bus.peutPartir():
                        bus.partir("Choucroutte")

                    else :
                        print("Le bus n'est pas partie.")

            finGenerale = False

        if choix == 6 :
            #Faire l'appel en tant que prof référent
            #Besoin : Rajouter la condition de vérification des bus
            #         Géré les mauvaises saisies
            choixBus = input("Quel bus ? ")

            for bus in listeBus :
                #Nécessite de vérifier que le bus de la liste est celui choisi
                if (False) :
                    bus.faireAppel()

            finGenerale = False

        if choix == 7 :
            #Quitter
            print("Enrevoir !")

        if choix == 8 :
            #Gestion des classes
            #Besoin : eleve.getNom et eleve.getPrenom possible ?
            #         Géré les mauvaises saisies
            print("Pas implémenter")
            print("Que voulez-vous faire ?")
            choix = int(input("1 : Ajouter une classe | 2 : Ajouter un élève dans une classe \n"))

            if choix == 1 :
                #Ajouter une classe
                listeClasse.append(Classe( input("Nombre maximum d'élèves dans la classe "), input("Nom de la classe : ")))

            if choix == 2 :
                #Ajouter un élève dans une classe
                choixClasse = int(input("Dans quel classe voulez-vous ajouter l'élève ?"))
                choixEleveNom = int(input("Nom de l'élève ?"))
                choixElevePrenom = int(input("Prénom de l'élève ?"))

                for listeClasse in classe :
                    if (classe.getNom == choixClasse) :
                        for listeEleve in eleve :
                            if (eleve.getNom == choixEleveNom and eleve.getPrenom == choixElevePrenom) :
                                classe.add_lyceen(eleve)

            finGenerale = False


else :
    print("Choix non valide !\n")
'''

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

bus1 = Bus("bus1")
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
#bus1.faireAppel()

if bus1.peutPartir():
    bus1.partir("Choucroutte")
