import requests
import sys
from classes import *
from interface import *
from PyQt5.QtWidgets import QApplication

print("Veuillez choisir la version à utilisé :")
choix = int(input("1 : Interface | 2 : Console \n"))

if choix == 1:
    ### On lance l'interface visuelle

    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())

if choix == 2:

    listeClasse = []
    listeEleve = []
    listeProf = []
    listeBus = []

    ### On lance la boucle de la version console
    finGenerale = False
    Tour = 0
    while not finGenerale:
        print("\nVeuillez choisir ce que vous voulez faire:\n")
        choix = int(input(
            "1 : Gestions des entitées \n2 : Gestion du départ des bus \n3 : Quitter\n4 : Initialiser un jeu de données\n"))

        if choix == 1:
            print("\nVeuillez choisir une action:\n")
            choixActionEntite = int(input(
                "1 : Saisir de nouveaux passagers \n2 : Saisir de nouveaux bus \n3 : Saisir une nouvelle classe \n4: Afficher la listes des entités\n"))

            if choixActionEntite == 1:
                # Passagers
                print("Quel est le passager ?")
                choixPassagers = int(input("1 : Elève | 2 : Professeur \n"))

                if choixPassagers == 1:
                    # Elève
                    print("Dans quelle classe ?\n")
                    classeEleve = input("Nom de la classe : \n")
                    found = False
                    for classe in listeClasse:
                        if classe.getNom() == classeEleve:
                            eleveNom = str(input("Nom de l'élève : \n"))
                            elevePrenom = str(input("Prenom de l'élève : \n"))
                            newLyceen = Lyceen(eleveNom, elevePrenom)
                            listeEleve.append(newLyceen)
                            classe.add_lyceen(newLyceen)
                            found = True
                            break
                    if not found:
                        print("La classe %s n'existe pas", classeEleve)

                if choixPassagers == 2:
                    # Professeur
                    profNom = str(input("Nom du professeur : \n"))
                    profPrenom = str(input("Prenom du professeur : \n"))
                    profReferent = True if (input("Référents ? (o/n)\n")) == "o" else False

                    listeProf.append(Prof(profReferent, profNom, profPrenom))

            elif choixActionEntite == 2:
                # Bus
                busNom = str(input("Nom du bus : \n"))
                placemaxBus = input("Nombre de places maximums dans le bus : \n")
                listeBus.append(Bus(busNom, placemaxBus))

            elif choixActionEntite == 3:
                # Classe
                classeTaille = int(input("Taille de la classe : \n"))
                classeNom = str(input("Nom de la classe : \n"))
                listeClasse.append(Classe(classeTaille, classeNom))

            elif choixActionEntite == 4:
                # AfficherListes
                if len(listeClasse) > 0:
                    print("\nListe des classes : \n")
                else:
                    print("\nIl n'y a aucune classe !")
                for classe in listeClasse:
                    print("    La classe " + classe.getNom(), " a un nombre maximum d'élèves de ", classe.getNbMax())

                if len(listeEleve) > 0:
                    print("\nListe des élèves : \n")
                    print("Nom:     " + "   " + "Prénom:")
                else:
                    print("\nIl n'y a aucun élève !")
                for eleve in listeEleve:
                    print("    " + eleve.getNom(), "       ", eleve.getPrenom())

                if len(listeProf) > 0:
                    print("\nListe des professeurs : \n")
                else:
                    print("\nIl n'y a aucun prof !")
                for prof in listeProf:
                    if prof.estReferent():
                        print("    " + prof.getNom(), " ", prof.getPrenom(), " est un professeur référent")
                    else:
                        print("    " + prof.getNom(), " ", prof.getPrenom(), " n'est pas un professeur référent")

                if len(listeBus) > 0:
                    print("\nListe des bus : \n")
                else:
                    print("\nIl n'y a aucun bus !")
                for bus in listeBus:
                    print("    " + bus.getNom(), " - ", bus.getNbPlacesMax(), " places maximum.")


        elif choix == 2:
            print("\nVeuillez choisir une action:\n")
            choixActionBus = int(input(
                "1 : Afficher les bus et leurs passagers \n2 : Faire monter un passager dans le bus\n3 : Faire l'appel dans un bus \n4 : Faire partir un bus\n"))

            if choixActionBus == 1:
                # AfficherBusEtPassagers
                print("Ils y a actuellement " + str(len(listeBus)) + " bus")
                for bus in listeBus:
                    print("\nLe bus " + bus.getNom() + " transporte " + str(len(bus.listPassager)) + " passagers")
                    print("    Ces passagers sont: ")

                    listpassager = "        "
                    for passager in bus.listPassager:
                        listpassager += passager.getPrenom() + " " + passager.getNom() + "; "
                    print(listpassager[:-1])

            elif choixActionBus == 2:
                # FaireMonterPassager
                print("Quel est le passager ?")
                choixPassagers = int(input("1 : Elève | 2 : Professeur \n"))
                if choixPassagers == 1:
                    eleveNom = str(input("Nom de l'élève à faire monter : \n"))
                    elevePrenom = str(input("Prenom de l'élève à faire monter : \n"))
                    nomBus = input("Nom du bus: \n")
                    for bus in listeBus:
                        if bus.getNom() == nomBus:
                            for eleve in listeEleve:
                                if eleve.getNom() == eleveNom and eleve.getPrenom() == elevePrenom:
                                    bus.add_passager(eleve)
                elif choixPassagers == 2:
                    profNom = str(input("Nom du prof à faire monter : \n"))
                    profPrenom = str(input("Prenom du prof à faire monter : \n"))
                    nomBus = input("Nom du bus: \n")
                    for bus in listeBus:
                        if bus.getNom() == nomBus:
                            for prof in listeProf:
                                if prof.getNom() == profNom and prof.getPrenom() == profPrenom:
                                    bus.add_passager(prof)

            elif choixActionBus == 3:
                # Faireappel
                nomBus = input("Nom du bus: \n")
                for bus in listeBus:
                    if bus.getNom() == nomBus:
                        try:
                            bus.faireAppel()
                            print("Le bus peux partir : L'appel à été fait avec succès!\n")

                        except EleveAbsentException:
                            print(
                                "Le bus ne peux pas partir car il y a au moins un élève absent et/ou n'a pas de classe\n")



            elif choixActionBus == 4:
                # FairePartirBus
                nomBus = input("Nom du bus a faire partir: \n")
                for bus in listeBus:
                    if bus.getNom() == nomBus:
                        if bus.peutPartir():
                            bus.partir(nomBus)
                        else:
                            print("L'appel n'a pas encore été fait et/ou validé !")
                        break

        elif choix == 3:
            finGenerale = True
        elif choix == 4:
            p1 = Prof(True, 'nomp1', 'prenomp1')
            p2 = Prof(False, 'nomp2', 'prenomp2')
            listeProf.extend([p1, p2])

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
            listeEleve.extend([e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11])

            classe1 = Classe(10, 'classe1')
            classe2 = Classe(10, 'classe2')
            classe3 = Classe(10, 'classe3')
            classe4 = Classe(10, 'classe4')
            listeClasse.extend([classe1, classe2, classe3, classe4])

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
            listeBus.append(bus1)

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

            print("\nJeu de données initialisé avec Succès !\n")
