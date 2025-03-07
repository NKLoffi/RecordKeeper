from database import Database
import sys
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QApplication, QMainWindow,
                              QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy)
from PyQt5.QtGui import QScreen, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize

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

        fname_label = QLabel("First Name: ")
        lname_label = QLabel("Last Name: ")
        email_label = QLabel("Email: ")
        dob_label = QLabel("DOB: ")
        sin_label = QLabel("SIN: ")
        addy_label = QLabel("Address: ")
        city_label = QLabel("City: ")
        province_label = QLabel("Province")

        self.fname_box = QLineEdit(self)
        self.lname_box  = QLineEdit(self)
        self.email_box = QLineEdit(self)
        self.dob_box = QLineEdit(self)
        self.sin_box = QLineEdit(self)
        self.addy_box = QLineEdit(self)
        self.city_box = QLineEdit(self)
        self.province_box = QLineEdit(self)


        self.fname_box.setPlaceholderText("eg. John")
        self.lname_box.setPlaceholderText("eg. Doe")
        self.email_box.setPlaceholderText("eg. doejohn@gmail.com")
        self.dob_box.setPlaceholderText("eg. DD-MM-YYYY")
        self.sin_box.setPlaceholderText("eg. 000-000-000")
        self.addy_box.setPlaceholderText("eg. 22 Devitt Ave N")
        self.city_box.setPlaceholderText("eg. Waterloo")
        self.province_box.setPlaceholderText("eg. Ontario")

        layout = QVBoxLayout()

        fname_layout = QHBoxLayout()
        fname_layout.addWidget(fname_label)
        fname_layout.addWidget(self.fname_box)

        lname_layout = QHBoxLayout()
        lname_layout.addWidget(lname_label)
        lname_layout.addWidget(self.lname_box)

        email_layout = QHBoxLayout()
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_box)

        dob_layout = QHBoxLayout()
        dob_layout.addWidget(dob_label)
        dob_layout.addWidget(self.dob_box)

        sin_layout = QHBoxLayout()
        sin_layout.addWidget(sin_label)
        sin_layout.addWidget(self.sin_box)

        addy_layout = QHBoxLayout()
        addy_layout.addWidget(addy_label)
        addy_layout.addWidget(self.addy_box)

        city_layout = QHBoxLayout()
        city_layout.addWidget(city_label)
        city_layout.addWidget(self.city_box)

        province_layout = QHBoxLayout()
        province_layout.addWidget(province_label)
        province_layout.addWidget(self.province_box)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)

        layout.addLayout(fname_layout)
        layout.addLayout(lname_layout)
        layout.addLayout(email_layout)
        layout.addLayout(dob_layout)
        layout.addLayout(sin_layout)
        layout.addLayout(addy_layout)
        layout.addLayout(city_layout)
        layout.addLayout(province_layout)
        layout.addLayout(button_layout)



        central_widget.setLayout(layout)
        layout.setSpacing(10)



        text_box = [self.fname_box, self.lname_box, self.email_box, self.dob_box, self.sin_box, self.addy_box, self.city_box, self.province_box]
        for box in text_box:
            box.setMinimumWidth(200)
            box.setAlignment(Qt.AlignLeft)
            box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        labels = [fname_label, lname_label, email_label, dob_label, sin_label, addy_label, city_label, province_label]
        for label in labels:
            label.setFixedWidth(100)


        fname_layout.addStretch()
        lname_layout.addStretch()
        email_layout.addStretch()
        dob_layout.addStretch()
        sin_layout.addStretch()
        addy_layout.addStretch()
        city_layout.addStretch()
        province_layout.addStretch()
        button_layout.addStretch()



        self.submit_button.setObjectName("submitButton")

        self.setStyleSheet("""
                           
            QMainWindow{
                background-color: #282C34;
            }
                           
            QPushButton#submitButton{

                background-color: #4CAF50;

                }
                           
            
            
            QLineEdit{
                background-color: #3E4451;
                margin-left: 10px;

                           }


        """)
    def submit_data(self):
        first_name = self.fname_box.text()
        last_name = self.lname_box.text()
        email = self.email_box.text()
        dob = self.dob_box.text()
        sin = self.sin_box.text()
        address = self.addy_box.text()
        city = self.city_box.text()
        province = self.province_box.text()

        self.db.insert_user_data(first_name, last_name, email, dob, sin, address, city, province)

        print("Data submitted successfully")
            

def main():
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()