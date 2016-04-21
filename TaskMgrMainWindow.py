import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from TaskMgrWidget import TaskMgrWidget


class TaskMgrMainWindow(QMainWindow):
    widget = None  # type:TaskMgrWidget

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.widget = TaskMgrWidget()

        self.setWindowTitle('Task Mgr')
        menubar = self.menuBar()
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        tasksMenu = menubar.addMenu('&Tasks')

        addTaskAction = QAction(QIcon('exit.png'), '&Add Task', self)
        addTaskAction.setShortcut('Ctrl+A')
        addTaskAction.setStatusTip('Add Task')
        addTaskAction.triggered.connect(self.widget.onAdd)
        tasksMenu.addAction(addTaskAction)

        detailsTaskAction = QAction(QIcon('exit.png'), 'Task Details', self)
        detailsTaskAction.setShortcut('Ctrl+D')
        detailsTaskAction.setStatusTip('Task Details')
        detailsTaskAction.triggered.connect(self.widget.onGetDetails)
        tasksMenu.addAction(detailsTaskAction)

        remTaskAction = QAction(QIcon('exit.png'), 'Delete Task(&X)', self)
        remTaskAction.setShortcut('Ctrl+X')
        remTaskAction.setStatusTip('Delete Task')
        remTaskAction.triggered.connect(self.widget.onDelete)
        tasksMenu.addAction(remTaskAction)

        refTaskAction = QAction(QIcon('exit.png'), '&Refresh', self)
        refTaskAction.setShortcut('Ctrl+R')
        refTaskAction.setStatusTip('Refresh Tasks')
        refTaskAction.triggered.connect(self.widget.onRefresh)
        tasksMenu.addAction(refTaskAction)

        self.setCentralWidget(self.widget)

        self.resize(250, 450)
        self.center()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TaskMgrMainWindow()
    t.show()
    sys.exit(app.exec_())
