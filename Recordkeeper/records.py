import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableView)
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
        self.setCentralWidget(self.table_view)

    def dataSearch():
        pass    

    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()