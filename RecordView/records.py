import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableView, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)
from PyQt5.QtSql import (QSqlDatabase, QSqlTableModel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database")
        self.resize(800, 800) # 800 pixels wide and tall
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data.db")
        if not db.open():
            sys.exit(-1)

        self.model = QSqlTableModel(self)
        self.model.setTable("info")
        self.model.select()

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setShowGrid(True)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search Data")

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.dataSearch)

        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_view)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.initUI()

    def dataSearch(self): # implement the function for searching a specific data from teh database
        search_text = self.search_input.text().strip()
        if search_text:
            self.model.setFilter(f"FirstName LIKE '%{search_text}%'")

        else:
            self.model.setFilter("")
        self.model.select()


    def initUI(self):
        self.setStyleSheet("""
            QWidget{
                background-color: hsl(220, 13%, 10%)
                           }

            QTableView{
                gridline-color:white;
                }
            """)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()