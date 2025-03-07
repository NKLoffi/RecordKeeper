from database import Database
import sys
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QApplication, QMainWindow,
                              QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()    # initalizing the main window

        self.db = Database()  #initalizing database connection 
        self.db.create_table() # To create table

        self.setWindowTitle("Information")  # setting title to the window
        self.resize(800, 800)  # 800 pixes wide and 800 pixels tall
        screen = QApplication.primaryScreen() # gets the primary screen (monitor) on which the application is running
        screen_react = screen.geometry() # Tells the program how big the entire screen is (Retrieves the geometry of the screen)
        window_react = self.frameGeometry() # Helps us understand how much space the window is taking  up
        window_react.moveCenter(screen_react.center()) # Finds the center point of the screen.

        self.setStyleSheet("background-color:rgb(40, 51, 58);") # background colour set to charcoal grey
        self.move(window_react.topLeft())

        self.submit_button = QPushButton("Submit") # Button for submit
        self.submit_button.clicked.connect(self.submit_data) 

        self.initUI()


        # Lets just make some text boxes for entering our data

    def initUI(self): # initalizing the UI
        central_widget = QWidget() 
        self.setCentralWidget(central_widget)

        self.labels = {                             # Stored the labels in Dictionary
            "fname": QLabel("First name: "),
            "lname": QLabel("Last Name: "),
            "email": QLabel("Email: "),
            "dob": QLabel("DOB: "),
            "sin": QLabel("SIN: "),
            "address" : QLabel("Address: "),
            "city": QLabel("City: "),
            "province": QLabel("Province")

        }

        self.text_boxes = {                     # Stored all the Text boxes in Dictionary
            "fname": QLineEdit(self),
            "lname": QLineEdit(self),
            "email": QLineEdit(self),
            "dob": QLineEdit(self),
            "sin": QLineEdit(self),
            "address": QLineEdit(self),
            "city": QLineEdit(self),
            "province": QLineEdit(self),
        }

        placeholders ={                        # Stored all placeholders in Dictionary
            "fname": "eg.John",
            "lname": "eg. doe",
            "email": "eg. doejohn@gmail.com",
            "dob": "eg. DD-MM-YYY",
            "sin": "eg. 000-000-000",
            "address": "eg. 22 Devitt Ave N",
            "city": "Waterloo",
            "province": "Ontario",
        }

        for key, textbox in self.text_boxes.items():
            textbox.setPlaceholderText(placeholders[key])
            textbox.setMinimumWidth(200)
            textbox.setAlignment(Qt.AlignLeft)
            textbox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout = QVBoxLayout()

        for key in self.labels:
            row_layout = QHBoxLayout()
            row_layout.addWidget(self.labels[key])
            self.labels[key].setFixedWidth(100)
            row_layout.addWidget(self.text_boxes[key])
            row_layout.addStretch()
            layout.addLayout(row_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        layout.setSpacing(10)

        self.submit_button.setObjectName("submitButton")

        self.setStyleSheet("""
                           
            QMainWindow{
                background-color: #282C34;
            }
                           
            QPushButton#submitButton{

                background-color: #4CAF50;
                color: white;

                }
                           
            
            QLineEdit{
                background-color: #3E4451;
                border: solid black;
                border-radius: 5px;
                margin-left: 10px;
                color: white;
                           }

            QLabel{
                color: white;
                           }
        """)
    def submit_data(self):

        first_name = self.text_boxes["fname"].text()
        last_name = self.text_boxes["lname"].text()
        email = self.text_boxes["email"].text()
        dob = self.text_boxes["dob"].text()
        sin = self.text_boxes["sin"].text()
        address = self.text_boxes["address"].text()
        city = self.text_boxes["city"].text()
        province = self.text_boxes["province"].text()

        self.db.insert_user_data(first_name, last_name, email, dob, sin, address, city, province)

        print("Data submitted successfully")
            

def main():
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()