import sys
# from Calcul import Calculator
from PyQt5 import QtCore, QtGui, QtWidgets
from calcul_pyqt import Ui_Dialog

class myCalc(QWidgets,QDialog):
    def __init__(self, parent=None):
        QtWidgets.QtWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = myCalc()
    myapp.show()
    sys.exit(app.exec_())