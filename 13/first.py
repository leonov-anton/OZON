import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton

# Создание приложения
app = QApplication(sys.argv)

# Создание окна
window = QWidget()

window.setGeometry(100, 100, 100, 100)
window.move(60, 15)
msg = QLabel('<h1>Hello!</h1>', parent=window)
msq.move(60, 15)

window.move(60, 50)
ok_button = QPushButton("OK", parent=window)
ok_button.move(60, 50)

window.show()
sys.exit(app.exec())

