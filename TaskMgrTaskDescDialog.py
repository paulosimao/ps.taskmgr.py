from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from TaskMgrFacade import TaskMgrFacade


class TaskMgrDeskDialog(QDialog):

    facade = None  # type:TaskMgrFacade

    def initUI(self, details):
        grid = QGridLayout()
        self.setLayout(grid)
        self.edit = QTextEdit(self)
        self.edit.setText(details['desc'])
        grid.addWidget(self.edit, 0, 0, 1, 1)
        self.edit.textChanged.connect(self.updateDesc)
        self.setWindowTitle("Dialog")
        self.setWindowModality(Qt.ApplicationModal)
        self.exec_()

    def updateDesc(self):
        try:
            self.widget.updateDesc(self.edit.toPlainText())
            self.widget.facade.updateOne(self.row, "desc", self.edit.toPlainText())

        except  Exception as e:
            print(e)

    def __init__(self, widget, row, details):
        super().__init__()
        self.widget = widget
        self.row = row
        self.initUI(details)
