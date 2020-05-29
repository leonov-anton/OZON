import sys
from Calcul import Calculator
from calculpyqt import *

class myCalc(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add)

    def add(self):
        x = float(self.ui.lineEdit.text())
        y = float(self.ui.lineEdit2.text())
        sum = x + y
        self.ui.label.setText(str(sum))







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = myCalc()
    myapp.show()
    sys.exit(app.exec_())

