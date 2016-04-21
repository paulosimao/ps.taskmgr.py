import sys
import TaskMgrTaskDescDialog
from PyQt5.QtWidgets import *
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

        id = str(item["_id"])
        self.table.setRowCount(c + 1)
        check = QTableWidgetItem();
        check.setCheckState(item["completed"])

        self.table.setItem(c, 0, check)
        self.table.setItem(c, 1, QTableWidgetItem(item["desc"]))

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
                self.facade.deleteOne(r.row())

            self.onRefresh()
        except Exception as e:
            print(e)

    def onGetDetails(self):
        for r in self.table.selectedIndexes():
            details = self.facade.getTaskDetails(r.row())
            t = TaskMgrTaskDescDialog.TaskMgrDeskDialog(self.facade, r.row(), details)
            print(details)

    def onItemChanged(self, item: QTableWidgetItem):
        if (item.column() == 0):
            self.facade.updateOne(item.row(), "completed", item.checkState())
        if (item.column() == 1):
            self.facade.updateOne(item.row(), "desc", item.text())

        self.table.resizeColumnsToContents()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('X'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Name'))

        grid.addWidget(self.table, 0, 0, 1, 1)

        self.onRefresh()
        self.table.resizeColumnsToContents()
        self.table.itemChanged.connect(self.onItemChanged)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TaskMgrWidget()
    t.show()
    sys.exit(app.exec_())
