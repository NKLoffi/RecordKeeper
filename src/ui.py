from database import Database
import sys
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QApplication, QMainWindow,
                              QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy,
                              QMessageBox)
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
import styles 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()    # initalizing the main window

        self.db = Database()  #initalizing database connection 
        self.db.create_table() # To create table    

        self.setWindowTitle("Record Keeper")  # setting title to the window
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
            "country" : QLabel("Country: "),
            "city": QLabel("City: "),
            "province": QLabel("Province: ")

        }
        
        self.text_boxes = {                     # Stored all the Text boxes in Dictionary
            "fname": QLineEdit(self),
            "lname": QLineEdit(self),
            "email": QLineEdit(self),
            "dob": QLineEdit(self),
            "sin": QLineEdit(self),
            "address": QLineEdit(self),
            "country": QLineEdit(self),
            "city": QLineEdit(self),
            "province": QLineEdit(self)
        }


        dob_regex = QRegularExpression(r"\d{2}-\d{2}-\d{4}") # Validator for date of birth
        self.text_boxes["dob"].setValidator(QRegularExpressionValidator(dob_regex, self)) # Assigned the validator for DOB text box

        sin_regex = QRegularExpression(r"\d{3}-\d{3}-\d{3}") # Validator for SIN number
        self.text_boxes["sin"].setValidator(QRegularExpressionValidator(sin_regex, self)) # Assigned the validator to SIN text box

        self.text_boxes["sin"].setEchoMode(QLineEdit.Password) #This will hide the SIN number when the user enters


        placeholders ={                        # Stored all placeholders in Dictionary
            "fname": "eg.John",
            "lname": "eg. doe",
            "email": "eg. doejohn@gmail.com",
            "dob": "eg. DD-MM-YYY",
            "sin": "eg. 000-000-000",
            "address": "eg. winter lane",
            "country": "eg. Canada",
            "city": "brightfox",
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
        # Adding .addStretch between and after the submit button will makesure the button is in center
        button_layout.addStretch()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch() 
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        layout.setSpacing(10)

        self.submit_button.setObjectName("submitButton")

        self.setStyleSheet(styles.WINDOW_STYLE)




    # Function to clear data after the user press Submit button

    def clear_data(self):  
        for textbox in self.text_boxes.values():
            textbox.clear()

    # Function to display a warning box for missing fields

    def warning_dialouge(self, empty_fields, invalid_email): 
        dialog = QMessageBox(self)
        dialog.setText("You need to fill all the fields")
        dialog.setWindowTitle("Warning") # the title is not displayed yet
        dialog.setIcon(QMessageBox.Information)

        if empty_fields:
            missing_fields_text = "\n".join([self.labels[key].text() for key in empty_fields]) 
            dialog.setDetailedText(f"You haven't filled the following fields:\n{missing_fields_text}")
        
        if invalid_email:
            dialog.setText("Invalid Email")
            dialog.setDetailedText("Please enter a valid email address.")
        dialog.exec_()

    def save_dialouge(self):
        dialog = QMessageBox(self)
        dialog.setText("Your data has been saved to our files")
        dialog.setWindowTitle("Success")
        dialog.setIcon(QMessageBox.Information)
        dialog.exec_()


    def submit_data(self): # function to save data to database

        empty_boxes = [key for key, textbox in self.text_boxes.items() if not textbox.text().strip()] 

        email = self.text_boxes["email"].text()
        email_regex = QRegularExpression(r"^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*@[0-9a-zA-Z]+([.-][0-9a-zA-Z]+)*\.[a-zA-Z]{2,}$")
        self.text_boxes["email"].setValidator(QRegularExpressionValidator(email_regex))
        invalid_email = not email_regex.match(email).hasMatch()

        if empty_boxes or invalid_email:
            self.warning_dialouge(empty_fields=  empty_boxes if empty_boxes else None, invalid_email = invalid_email)
            return
            

        first_name = self.text_boxes["fname"].text()
        last_name = self.text_boxes["lname"].text()
        email = self.text_boxes["email"].text()
        dob = self.text_boxes["dob"].text()
        sin = self.text_boxes["sin"].text()
        address = self.text_boxes["address"].text()
        country = self.text_boxes["country"].text()
        city = self.text_boxes["city"].text()
        province = self.text_boxes["province"].text()

        self.db.insert_user_data(first_name, last_name, email, dob, sin, address, country, city, province)

        print("Data submitted successfully")

        self.save_dialouge() # Called the message box to show the user the data is saved to the database

        self.clear_data() # Called the function to clear data After the user clickes submit button