import sys
import CustomModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CustomDelegate(QItemDelegate):
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        ret = QComboBox(QWidget)
        ret.addItem("a")
        ret.addItem("b")
        ret.addItem("c")
        return ret

    def setEditorData(self, QWidget, QModelIndex):
        value = QModelIndex.model().data(QModelIndex, Qt.EditRole)
        QWidget.setCurrentIndex(QWidget.findText(value))

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        value = QWidget.currentText()
        QAbstractItemModel.setData(QModelIndex,value,Qt.EditRole)

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QWidget.setGeometry(QStyleOptionViewItem.rect)
