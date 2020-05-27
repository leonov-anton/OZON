import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Форма")
layout = QVBoxLayout()
layout.addWidget(QPushButton("Верх"))
layout.addWidget(QPushButton("Центр"))
layout.addWidget(QPushButton("Низ"))

window.setLayout(layout)
window.show()
sys.exit(app.exec_())