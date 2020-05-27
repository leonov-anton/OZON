import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Форма")
layout = QGridLayout()

layout.addWidget(QPushButton("00"), 0, 0)
layout.addWidget(QPushButton("01"), 0, 1)
layout.addWidget(QPushButton("02"), 0, 2)
layout.addWidget(QPushButton("03"), 0, 3)
layout.addWidget(QPushButton("10"), 1, 0)
layout.addWidget(QPushButton("11"), 1, 1)
layout.addWidget(QPushButton("12"), 1, 2)
layout.addWidget(QPushButton("13"), 1, 3)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

# layout.addRow("Имя: ", QLineEdit())
# layout.addRow("Фамилия: ", QLineEdit())
# layout.addRow("Возраст: ", QLineEdit())
# layout.addRow(QPushButton())
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())
