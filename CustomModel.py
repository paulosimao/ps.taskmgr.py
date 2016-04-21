import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CustomModel(QAbstractTableModel):
    def __init__(self, columns, parent=None):
        super(CustomModel, self).__init__(parent)
        self.columns = columns
        self.datatable = []

    def columnCount(self, QModelIndex_parent=None):
        return len(self.columns)

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section].title()

    def rowCount(self, QModelIndex_parent=None):
        return len(self.datatable)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = self.datatable[index.row()]
            column_key = self.columns[index.column()]
            return row[column_key]
        else:
            return None

    def setData(self, index, value, int_role=None):
        if (len(self.datatable) > index.row()):
            self.datatable.append(["", ""])

        row = self.datatable[index.row()]
        column_key = self.columns[index.column()]
        row[column_key] = value


        # def flags(self, QModelIndex):
        #     return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        #
        # def insertRow(self, p_int, QModelIndex_parent=None):
        #     # self.beginInsertRows()
        #     self.datatable.append(["", ""])
        #     # self.endInsertRows()
