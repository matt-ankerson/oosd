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

        # set the subject
        self.user1.set_subject(self.user0)
        self.user2.set_subject(self.user0)

        # set the 'twitter feeds' to read only.
        self.txtUser1.setReadOnly(True)
        self.txtUser2.setReadOnly(True)

        # handle the "editingFinished event"
        self.txtMessage.editingFinished.connect(self.update_message)

    def update_message(self):
        new_message = str(self.txtMessage.text())
        self.user0.send_tweet = new_message # will trigger the __setattr__ method of user0.
        self.txtUser1.append(str(self.user1.receive_tweet))
        self.txtUser2.append(str(self.user2.receive_tweet))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())