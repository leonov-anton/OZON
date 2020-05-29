import sys
from Calcul import Calculator
from calculpyqt import *

class myCalc(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.dif)
        self.ui.pushButton_3.clicked.connect(self.mult)
        self.ui.pushButton_4.clicked.connect(self.div)
        self.ui.pushButton_5.clicked.connect(self.exp)
        self.ui.pushButton_6.clicked.connect(self.sqr)

        self.show()

    def add(self):
        # x = self.ui.lineEdit.text()
        # y = self.ui.lineEdit2.text()
        # z = int(x) + int(y)
        self.ui.label.setText()

    def dif(self):
        # x = int(self.ui.lineEdit.text())
        # y = int(self.ui.lineEdit2.text())
        # z = x * y
        self.ui.label.setText()

    def mult(self):
        # x = int(self.ui.lineEdit.text())
        # y = int(self.ui.lineEdit2.text())
        # z = x * y
        self.ui.label.setText("milt")

    def div(self):
        # x = int(self.ui.lineEdit.text())
        # y = int(self.ui.lineEdit2.text())
        # z = x * y
        self.ui.label.setText("div")

    def exp(self):
        # x = int(self.ui.lineEdit.text())
        # y = int(self.ui.lineEdit2.text())
        # z = x * y
        self.ui.label.setText("exp")

    def sqr(self):
        # x = int(self.ui.lineEdit.text())
        # y = int(self.ui.lineEdit2.text())
        # z = x * y
        self.ui.label.setText("sqr")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = myCalc()
    sys.exit(app.exec_())

