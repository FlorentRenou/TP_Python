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
                if self.listPassager[i].estAbsent() or not self.listPassager[i].hasClasse():
                    self.appel = False
            i += 1

    def troisClassesMax(self):
        listeClassePresenteBus = []
        for passager in self.listPassager:
            if type(passager) is Lyceen:
                if passager.getClasse() not in listeClassePresenteBus:
                    listeClassePresenteBus.append(passager.getClasse())
        return len(listeClassePresenteBus)<=3

    def unProfReferent(self):
        profReferentPresent = False
        for passager in self.listPassager:
            if type(passager) is Prof:
                if passager.estReferent():
                    if profReferentPresent == False:
                        profReferentPresent = True
                    else:
                        return False
        return profReferentPresent

    def unProfPourDixLyceen(self):
        nbProf = 0
        nbEleve = 0
        for passager in self.listPassager:
            if type(passager) is Prof:
                nbProf +=1
            else : 
                nbEleve +=1
        return nbEleve / nbProf <=10


    def peutPartir(self):
        return self.appelIsOk() and len(
            self.listPassager) > 0 and self.troisClassesMax() and self.unProfReferent() and self.unProfPourDixLyceen()

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
        self.nom = nom
        self.listLyceen = []

    def add_lyceen(self, lyceen):
        if len(self.listLyceen)<self.nbMax:
            self.listLyceen.append(lyceen)
            lyceen.setNomClasse(self.nom)

    def getNom(self):
        return self.nom

    def getNbMax(self):
        return self.nbMax
