import sys
from PyQt4 import QtCore, QtGui, uic
from user import User

# Author: Matt Ankerson
# Date: 27 March 2015

qtCreatorFile = "dashboard.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DashApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # set up our three users
        self.user0 = User()
        self.user1 = User()
        self.user2 = User()

        # handle the "editingFinished event"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())