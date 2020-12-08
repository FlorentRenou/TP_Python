import random


class Bus:
    def __init__(self):
        self.nbPlacesMax = random.randrange(20, 60, 1)
        self.appel = True  # Faire une liste des personnes absentes
        self.listPassager = []

    def add_passager(self, passager):
        if len(self.listPassager) < self.nbPlacesMax:
            self.listPassager.append(passager)

    def getNbPlacesMax(self):
        return self.nbPlacesMax

    def appelIsOk(self):
        return self.appel

    def faireAppel(self):
        i = 0
        while self.appel and i <= len(self.listPassager) - 1:
            if type(self.listPassager[i]) is Lyceen:
                if self.listPassager[i].estAbsent():
                    self.appel = False
            i += 1

    def troisClassesMax(self):
        return 1

    def unProfReferentEtUnProfPourDixLyceen(self):
        return 1

    def peutPartir(self):
        return self.appelIsOk() and len(
            self.listPassager) > 0 and self.troisClassesMax() and self.unProfReferentEtUnProfPourDixLyceen()

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


class Classe:
    def __init__(self, nbMax, nom):
        self.nbMax = nbMax
        self.nom = nom
        self.listLyceen = []

    def add_lyceen(self, lyceen):
        self.listLyceen.append(lyceen)
        lyceen.setNomClasse(self.nom)

    def getNom(self):
        return self.nom

    def getNbMax(self):
        return self.nbMax
