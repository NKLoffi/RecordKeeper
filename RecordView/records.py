import sys
from PyQt5.QtWidgets import (QMainWindow, QTableView, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtSql import (QSqlDatabase, QSqlTableModel)
import styles

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

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        search_container = QWidget()
        search_container.setLayout(search_layout)

        layout = QVBoxLayout()
        layout.addWidget(search_container)
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
        self.setStyleSheet(styles.WINDOW_STYLE)
        