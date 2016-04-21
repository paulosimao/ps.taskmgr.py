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
        QAbstractItemModel.setData(QModelIndex, value, Qt.EditRole)

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QWidget.setGeometry(QStyleOptionViewItem.rect)

        # def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        #     try:
        #         c = QStyleOptionComboBox()
        #         # r = QStyleOptionViewItem.rect
        #         # c.
        #         QApplication.style().drawControl(QStyle.CE_ComboBoxLabel, c, QPainter)
        #     except Exception as e:
        #         print(e)


class DateCalendarDelegate(QItemDelegate):
    date = None  # type:QDate
    table = None  # type:QTableView

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        d = QDialog()
        cal = QCalendarWidget(QWidget)
        grid = QGridLayout()
        d.setLayout(grid)
        grid.addWidget(cal, 0, 0, 1, 1)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()
        try:
            dt = str(cal.selectedDate().year()) + '.' + ('0'+str(cal.selectedDate().month()))[-2:] + '.' + ('0'+str(cal.selectedDate().day()))[-2:]
            self.table.setItem(QModelIndex.row(), QModelIndex.column(), QTableWidgetItem(dt))
        except Exception as e:
            print(e)
        # return cal
        print(cal.selectedDate())

    def setEditorData(self, QWidget, QModelIndex):
        value = QModelIndex.model().data(QModelIndex, Qt.EditRole)
        QWidget.setCurrentIndex(QWidget.findText(value))

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        value = QWidget.currentText()
        QAbstractItemModel.setData(QModelIndex, value, Qt.EditRole)
