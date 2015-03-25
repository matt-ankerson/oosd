import sys
from PyQt4 import QtCore, QtGui, uic
from bicycle import Bicycle
from speedometer import Speedometer
from calorie_meter import CalorieMeter

# Author: Matt Ankerson
# Date: 25 March 2015

# this is the gui xml schema file
qtCreatorFile = "dashboard.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DashApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # set up the bicycle and our speedo and calorie meter
        self.push_bike = Bicycle()
        self.speedometer = Speedometer(self.push_bike)
        self.calorie_meter = CalorieMeter(self.push_bike)

        # handle the "editingFinished" event
        self.txtRpms.editingFinished.connect(self.update_rpms)

    def update_rpms(self):
        new_rpms = int(self.txtRpms.text())
        self.push_bike.current_rpms = new_rpms # set the rpms (will trigger the __setattr__() method)
        self.txtSpeed.setText(str(self.speedometer.speed))
        self.txtCalories.setText(str(self.calorie_meter.calories))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())