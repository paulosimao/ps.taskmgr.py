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
        # self.setWindowTitle("PyQt Dialog demo")
        # self.show()
        self.edit.textChanged.connect(self.updateDesc)
        self.setWindowTitle("Dialog")
        self.setWindowModality(Qt.ApplicationModal)
        self.exec_()

    def updateDesc(self):
        try:
            self.facade.updateOne(self.row, "desc", self.edit.toPlainText())
        except  Exception as e:
            print(e)

    def __init__(self, facade, row, details):
        super().__init__()
        self.facade = facade
        self.row = row
        self.initUI(details)
