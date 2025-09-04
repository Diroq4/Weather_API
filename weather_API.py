import sys #Handles system variables for the python interpreter
import requests #This is to have the posibility to make a request from an API
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt #This import will give us the posibility to work with aligment

#Setting the variables and initializing the UI
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input_label = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temp_label = QLabel("70 °C", self)
        self.emoji_label = QLabel("🔆", self)
        self.description_weather_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

#Edit the way they show, order vertically
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input_label)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_weather_label)

        self.setLayout(vbox)

#Align to the center of the Window
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_weather_label.setAlignment(Qt.AlignCenter)

#Apply CSS Style
        self.city_label.setObjectName("city_label")
        self.city_input_label.setObjectName("city_input_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_weather_label.setObjectName("description_weather_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;       
            }
            QLabel#city_label{
                font-size: 50px;
                font-style: italic;               
            }
            QLineEdit#city_input_label{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-syle: bold;
            }           
            QLabel#temp_label{
                font-size: 75px;               
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;               
            }
            QLabel#description_weather_label{
                font-size: 50px;               
            }
                            """)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())