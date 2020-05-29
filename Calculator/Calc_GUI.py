import sys
from calul_pyqt import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = exemple()
    myapp.show()
    sys.exit(app.exec_())

