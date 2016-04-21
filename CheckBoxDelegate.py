import sys
import CustomModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CheckBoxDelegate(QItemDelegate):
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        ret = QCheckBox(QWidget)
        return ret

    def setEditorData(self, QWidget, QModelIndex):
        value = QModelIndex.model().data(QModelIndex, Qt.EditRole)
        QWidget.setChecked(value == "X")

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        if QWidget.isChecked():
            value = "X"
        else:
            value = ""

        QAbstractItemModel.setData(QModelIndex, value, Qt.EditRole)

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QWidget.setGeometry(QStyleOptionViewItem.rect)
