from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from meteofrance_api import MeteoFranceClient

import requests


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

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

        layout.addWidget(metteo_label)
        layout.addWidget(last_button)
        layout.addWidget(next_button)
        layout.addWidget(new_button)

        layout.addWidget(self.label)

        self.setLayout(layout)

        self.show()
