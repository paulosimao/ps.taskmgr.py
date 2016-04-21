import sys
import TaskMgrTaskDescDialog
from CustomDelegate import DateCalendarDelegate
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from TaskMgrFacade import TaskMgrFacade


class TaskMgrWidget(QWidget):
    table = None  # type : QTableWidget
    facade = None  # type : TaskMgrFacade

    def __init__(self):
        super().__init__()
        self.facade = TaskMgrFacade()
        self.initUI()

    def addItem(self, item: dict):
        print(item)
        c = self.table.rowCount();

        self.table.setRowCount(c + 1)
        check = QTableWidgetItem(item["desc"]);
        check.setCheckState(item["completed"])

        self.table.setItem(c, 0, QTableWidgetItem(str(item["_id"])))
        self.table.setItem(c, 1, check)
        if 'duedate' in item:
            self.table.setItem(c, 2, QTableWidgetItem(item["duedate"]))
            # point = QPoint(c, 2)
            # point = self.table.model().index(c, 2)
            # index = self.table.indexAt(point)
            # self.table.setIndexWidget(point, QCalendarWidget())

    def onAdd(self):
        try:
            d = self.facade.createNew()
        except Exception as e:
            print(e)

        self.addItem(d)

    def onRefresh(self):
        while self.table.rowCount() > 0:
            self.table.removeRow(0)

        for t in self.facade.getTasks():
            self.addItem(t)

    def onDelete(self):
        try:
            for r in self.table.selectedIndexes():
                id = self.table.item(r.row(), 0).text()
                self.facade.deleteOne(id)

            self.onRefresh()
        except Exception as e:
            print(e)

    def onGetDetails(self):
        for r in self.table.selectedIndexes():
            id = self.table.item(r.row(), 0).text()
            details = self.facade.getTaskDetails(id)
            t = TaskMgrTaskDescDialog.TaskMgrDeskDialog(self, r.row(), details)
            print(details)

    def updateDesc(self, text):
        item = self.table.selectedItems()[0]  # type:QTableWidgetItem
        item.setText(text)

    def onItemChanged(self, item: QTableWidgetItem):
        id = self.table.item(item.row(), 0).text()
        if (item.column() == 1):
            self.facade.updateOne(id, "desc", item.text())
            self.facade.updateOne(id, "completed", item.checkState())
        if (item.column() == 2):
            self.facade.updateOne(id, "duedate", item.text())

        self.table.resizeColumnsToContents()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setColumnHidden(0, True)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Task'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Due Date'))

        self.table.setSortingEnabled(True)
        cd = DateCalendarDelegate()

        cd.table = self.table

        self.table.setItemDelegateForColumn(2, cd)
        grid.addWidget(self.table, 0, 0, 1, 1)

        self.onRefresh()
        self.table.resizeColumnsToContents()
        self.table.itemChanged.connect(self.onItemChanged)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TaskMgrWidget()
    t.show()
    sys.exit(app.exec_())
