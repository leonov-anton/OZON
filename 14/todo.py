import sys
import json
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt

design_path = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(design_path)
tick = QtGui.QImage('tick.png')
tick2 = QtGui.QImage('tick2.png')

class TodoModel(QtCore.QAbstractListModel):

    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
            else:
                return tick2

    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.ui.todoView.setModel(self.model)
        self.ui.addButton.pressed.connect(self.add)
        self.ui.deleteButton.pressed.connect(self.delete)
        self.ui.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.ui.todoEdit.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.ui.todoEdit.setText("")
            self.save()

    def delete(self):
        indexes = self.ui.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.ui.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.ui.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            ststus, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index,index)
            self.ui.todoView.clearSelection()
            self.save()

    def save(self):
        file = open('data.db', 'w')
        data = json.dump(self.model.todos, file)
        file.close()

    def load(self):
        try:
            file = open('data.db', 'r')
            self.model.todos = json.load(file)
            file.close()
        except Exception:
            pass

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
