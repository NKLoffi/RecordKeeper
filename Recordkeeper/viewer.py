from database import Database
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableView)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Base Viewer")
        self.resize(800, 800) # 800 pixels wide and 800 pixels tall
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.db")

        self.model = QSqlTableModel(self)
        self.model.setTable("info")
        self.model.select()

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.setCentralWidget(self.table_view)

        self.initUI()


    def initUI(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: hsl(188, 33%, 8%)
                           }

            """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()

