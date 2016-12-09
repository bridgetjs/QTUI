from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
import sys
import os
os.system("pyuic5 attempt2.ui -o attempt2.py")
import attempt2
import time
import numpy as np

Name= 'Some Name '

class ExampleApp(QtWidgets.QWidget, attempt2.Ui_Form):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()

        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        self.RefreshB.clicked[bool].connect(self.Refresh)
        QTimer.singleShot(1000,  lambda: self.Refresh())

    def Refresh(self):
        Thing2_Value = np.random.randint(3)

        self.Value_1.setText("%d" %Thing2_Value )
        self.SetColor(source=Thing2_Value)

        QTimer.singleShot(1000, lambda: self.Refresh())

    def SetColor(self,source):
        col = QColor(0, 0, 0)
        self.Value_1.setStyleSheet("QLabel { background-color : %s}" % col.name())
        val=255
        if source==0:
            col.setRed(val)
        elif source==1:
            col.setRed(val)
            col.setGreen(val)
        elif source==2:
            col.setGreen(val)

        self.Value_1.setStyleSheet("QLabel { background-color : %s}" %col.name()  )


def main():

    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form

    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function