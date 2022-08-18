# ************************** man hinh loai 2 *************************
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # add row and column count
        self.uic.tableWidget.setColumnCount(4)
        self.uic.tableWidget.setRowCount(8)

        # set column width
        for m in range(1, 4):
            self.uic.tableWidget.setColumnWidth(m, 50)

        # set row height
        for n in range(6):
            self.uic.tableWidget.setRowHeight(n, 100)

        # add button to QTableWidget
        for i in range(6):
            self.row = i
            btn = QPushButton('Button num {}'.format(i))
            btn.clicked.connect(self.handleButtonClicked)
            self.uic.tableWidget.setCellWidget(self.row, 0, btn)

    # position of clicked button
    def handleButtonClicked(self):
        # button = QApplication.focusWidget()
        button = self.sender()
        index = self.uic.tableWidget.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())
            self.add_image(index.row())

    # add image to QLabelWidget
    def add_image(self, row):
        print("row", row)
        link = QFileDialog.getOpenFileName(filter="*.jpg *.jpeg *.png")
        image = QLabel()
        image.setStyleSheet("border-image: url({});".format(link[0]))
        self.uic.tableWidget.setCellWidget(row, 0, image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())