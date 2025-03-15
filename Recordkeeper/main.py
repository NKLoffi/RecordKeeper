from database import Database
import sys
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QApplication, QMainWindow,
                              QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy,
                              QMessageBox)
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator

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
            "country" : QLabel("Country"),
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
            "country": QLineEdit(self),
            "city": QLineEdit(self),
            "province": QLineEdit(self),
        }


        dob_regex = QRegularExpression(r"\d{2}-\d{2}-\d{4}") # Validator dor date of birth
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
            "address": "eg. 22 Devitt Ave N",
            "country": "eg. Canada",
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
        # Adding .addStretch between and after the submit button will makesure the button is in center
        button_layout.addStretch()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch() 
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        layout.setSpacing(10)

        self.submit_button.setObjectName("submitButton")

        self.setStyleSheet("""
                           
            QMainWindow{
                background-color: hsl(220, 13%, 16%)
            }
                           
            QPushButton#submitButton{

                background-color: hsl(122, 39%, 49%);
                color: white;
                min-width: 100px;
                max-width: 100px;
                min-height: 25px;
                max-height: 25px;
                border-radius: 5px;


                }
            QPushButton#submitButton:hover {
                           background-color: hsl(122, 39%, 40%);

                           
                           }
                           
            
            QLineEdit{
                background-color: hsl(221, 13%, 28%);
                border: solid black;
                border-radius: 5px;
                margin-left: 10px;
                min-width: 200px;
                max-width: 200px;
                min-height: 25px;
                max-height: 25px;
                color: white;
                           }

            QLabel{
                color: white;
                           }
        """)


        # Function to clear data after the user press Submit button

    def clear_data(self):  
        for textbox in self.text_boxes.values():
            textbox.clear()

    def submit_data(self): # function to save data to database

        empty_boxes = [key for key, textbox in self.text_boxes.items() if not textbox.text().strip()] 

        if empty_boxes:
            QMessageBox.warning(self,"Missing Fields", "All fields Are Required")
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

        self.clear_data() # Called the function to clear data After the user clickes submit button
        
def main():
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()