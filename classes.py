import random
from exception import *


class Bus:
    def __init__(self):
        self.nbPlacesMax = random.randrange(20, 60, 1)
        self.appel = True  # Faire une liste des personnes absentes
        self.listPassager = []

    def add_passager(self, passager):
        if len(self.listPassager) < self.nbPlacesMax:
            self.listPassager.append(passager)
        else:
            raise LimitePassagerDepasserException

    def getNbPlacesMax(self):
        return self.nbPlacesMax

    def appelIsOk(self):
        # Besoin d'une exception ?
        return self.appel

    def faireAppel(self):
        i = 0
        while self.appel and i <= len(self.listPassager) - 1:
            if type(self.listPassager[i]) is Lyceen:
                if self.listPassager[i].estAbsent() or not self.listPassager[i].hasClasse():
                    self.appel = False
                    raise EleveAbsentException
            i += 1

    def troisClassesMax(self):
        listeClassePresenteBus = []
        for passager in self.listPassager:
            if type(passager) is Lyceen:
                if passager.getClasse() not in listeClassePresenteBus:
                    listeClassePresenteBus.append(passager.getClasse())
        if len(listeClassePresenteBus) <= 3:
            return True
        else:
            raise LimiteClasseDepasserException
        # return len(listeClassePresenteBus)<=3

    def unProfReferent(self):
        profReferentPresent = False
        for passager in self.listPassager:
            if type(passager) is Prof:
                if passager.estReferent():
                    if not profReferentPresent:
                        profReferentPresent = True
                    else:
                        raise NombreProfReferentException
        return profReferentPresent
        # return profReferentPresent

    def unProfPourDixLyceen(self):
        nbProf = 0
        nbEleve = 0
        for passager in self.listPassager:
            if type(passager) is Prof:
                nbProf += 1
            else:
                nbEleve += 1
        if nbEleve / nbProf <= 10:
            return True
        else:
            raise LimiteProfParEleveDepasserException
        # return nbEleve / nbProf <=10

    def peutPartir(self):
        # Besoin d'une exception ?
        try :
            return self.appelIsOk() and len(self.listPassager) > 0 and self.troisClassesMax() and self.unProfReferent() and self.unProfPourDixLyceen()
        except LimitePassagerDepasserException:
            print("Il y a trop de passager")
        except EleveAbsentException:
            print("Il y a un élève absent")
        except LimiteClasseDepasserException:
            print("Il y a trop de classe dans le même bus")
        except NombreProfReferentException:
            print("Il n'y a pas le bon nombre de professeur référent")
        except LimiteProfParEleveDepasserException:
            print("Il n'y a pas assez de professeur")

    def partir(self, nom):
        print('Le bus %s est parti' % nom)


class Passager:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Prof(Passager):
    def __init__(self, referent, nom, prenom):
        super().__init__(nom, prenom)
        self.referent = referent

    def estReferent(self):
        return self.referent


class Lyceen(Passager):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.absent = False
        self.nomClasse = None

    def setNomClasse(self, nomClasse):
        self.nomClasse = nomClasse

    def estAbsent(self):
        if random.randrange(0, 100, 1) <= 1:
            self.absent = True
        return self.absent

    def getClasse(self):
        return self.nomClasse

    def hasClasse(self):
        return self.nomClasse != None


class Classe:
    def __init__(self, nbMax, nom):
        self.nbMax = nbMax
        # Need gestion unicité pour le nom
        self.nom = nom
        self.listLyceen = []

    def add_lyceen(self, lyceen):
        if len(self.listLyceen) < self.nbMax:
            self.listLyceen.append(lyceen)
            lyceen.setNomClasse(self.nom)
        else:
            raise LimiteEleveDepasserException

    def getNom(self):
        return self.nom

    def getNbMax(self):
        return self.nbMax
