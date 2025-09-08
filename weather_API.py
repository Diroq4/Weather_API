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
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_weather_label = QLabel(self)
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
                font-style: bold;
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
        
        self.get_weather_button.clicked.connect(self.get_weather)

#Connecting to the API
    def get_weather(self):
        api_key = "c8adbf13b8b1778b7906b4a1e1cfadde"
        city = self.city_input_label.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

#Here we create messages in case a bad or lost connection with the API
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \n Please check your input")
                case 401:
                    self.display_error("Unauthorized: \n Invalid API")
                case 403:
                    self.display_error("Access denied")
                case 404:
                    self.display_error("Not found: \nCity not found")
                case 500:
                    self.display_error("Server error: \nTry later")
                case 502:
                    self.display_error("Bad getaway: \nInvalid response from server")
                case 503:
                    self.display_error("Service unavailable: \nServer is down")
                case 504:
                    self.display_error("Getaway timeout: \nNo response from server")
                case _:
                    self.display_error("HTTP error occured")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\nThe request timeout")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects error:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")

    def display_error(self, message):
#We just take the error messages from the get weather fuction and display it on the app
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)

    def display_weather(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())