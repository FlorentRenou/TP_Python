from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit,QComboBox, QCheckBox
from meteofrance_api import MeteoFranceClient
from PyQt5.QtCore import Qt
import requests
from classes import *


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.listeClasse = []
        self.listeEleve = []
        self.listeProf = []
        self.listeBus = []


    def get_meteo(self):
        client = MeteoFranceClient()

        marseille = client.search_places('Marseille')[0]
        current_forecast = client.get_forecast_for_place(marseille).current_forecast

        return current_forecast

    def initUI(self):
        self.setGeometry(100, 60, 1000, 800)
        

        layout = QVBoxLayout()
        
        self.label = QLabel("")
        metteo = self.get_meteo()
        metteo_label = QLabel(
            f"Il fait {metteo['T']['value']}°C, Humidité: {metteo['humidity']} à Marseille aujourd'hui")

        self.setWindowTitle('Voyage scolaire')
        last_button = QPushButton('Saisir de nouveaux profs', self)
        ###last_button.clicked.connect(self.previous_joke)

        next_button = QPushButton('Saisir de nouveaux lycéens', self)
        ###next_button.clicked.connect(self.next_joke)

        new_button = QPushButton('Faire l\'appel', self)
        ###new_button.clicked.connect(self.new_joke)


        # Ajout de nouveaux passagers
        labelProfLyceen = QLabel("Créer un nouveau passager : ")
        self.caseProf = QCheckBox("Prof")
        self.caseLyceen = QCheckBox("Lycéen")
        self.nomPassager = QLineEdit("NOM")
        self.prenomPassager = QLineEdit("PRENOM")
        self.labelReferent = QLabel("Référent ?")
        self.caseReferentOui = QCheckBox("Oui")
        self.caseReferentNon = QCheckBox("Non")
        self.comboClasse = QComboBox(self)
        #for classe in self.listeClasse :
        #    self.comboClasse.addItem(classe.nom())
        
        btnAjouterPassager = QPushButton('Valider', self)
        btnAjouterPassager.clicked.connect(self.ajouterPassager)

        # Changement état CheckBox
        self.caseProf.stateChanged.connect(self.etat_changeP)
        self.caseLyceen.stateChanged.connect(self.etat_changeL)
        self.caseReferentOui.stateChanged.connect(self.etat_changeROui)
        self.caseReferentNon.stateChanged.connect(self.etat_changeRNon)



        layout.addWidget(metteo_label)
        layout.addWidget(last_button)
        layout.addWidget(next_button)
        layout.addWidget(new_button)

        # Ajout de nouveaux passagers
        layout.addWidget(labelProfLyceen)
        layout.addWidget(self.caseProf)
        layout.addWidget(self.caseLyceen)
        layout.addWidget(self.nomPassager)
        layout.addWidget(self.prenomPassager)
        layout.addWidget(self.labelReferent)
        layout.addWidget(self.caseReferentOui)
        layout.addWidget(self.caseReferentNon)
        layout.addWidget(self.comboClasse)
        layout.addWidget(btnAjouterPassager)
        self.labelReferent.hide()
        self.caseReferentOui.hide()
        self.caseReferentNon.hide()
        self.comboClasse.hide()

        layout.addWidget(self.label)

        self.setLayout(layout)

        self.show()
<<<<<<< HEAD


    def etat_changeP(self):
        if self.caseProf.checkState() == Qt.Checked:
            self.caseLyceen.setChecked(False)
            self.labelReferent.show()
            self.caseReferentOui.show()
            self.caseReferentNon.show()
            self.comboClasse.hide()
        else:
            print("decoche")

    def etat_changeL(self):
        if self.caseLyceen.checkState() == Qt.Checked:
            self.caseProf.setChecked(False)
            self.labelReferent.hide()
            self.caseReferentOui.hide()
            self.caseReferentNon.hide()
            self.comboClasse.show()
        else:
            print("decoche") 
    
    def etat_changeROui(self):
        if self.caseReferentOui.checkState() == Qt.Checked:
            self.caseReferentNon.setChecked(False)
        else:
            print("decoche")

    def etat_changeRNon(self):
        if self.caseReferentNon.checkState() == Qt.Checked:
            self.caseReferentOui.setChecked(False)
        else:
            print("decoche") 
    
    def ajouterPassager(self):
        # Si le nom n'est pas vide
        if self.nomPassager.text() !="" or self.prenomPassager.text() != "":
            # Si c'est un lyceen
            if self.caseLyceen.checkState() == Qt.Checked:
                self.listeEleve.append(Lyceen(self.nomPassager, self.prenomPassager))
                self.comboClasse.currentText.add_lyceen(self.listeEleve[-1])
            
            # Si c'est un prof
            if self.caseProf.checkState() == Qt.Checked:
                if self.caseReferentOui.checkState() == Qt.Checked:
                    
                    self.listeProf.append(Prof(True, self.nomPassager, self.prenomPassager))
                else :
                    self.listeProf.append(Prof(False, self.nomPassager, self.prenomPassager))
                print(len(self.listeProf))
        else :
            NomImpossibleException()

        


    
=======
>>>>>>> 01c467384edb91611944ea998e04ce4a8b121f9e
