from kiwoom.kiwoom_01 import *

import sys
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print("Ui_class")

        self.app = QApplication(sys.argv)

        self.kiwoom = Kiwoom()

        self.app.exec_()


