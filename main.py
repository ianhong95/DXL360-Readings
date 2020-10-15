from readingUI import UIController, readingUI
from PyQt5 import QtWidgets

import sys

from SerialObjClass import SerialObj as cereal


def main():
    pass


if __name__ == '__main__':

    DXL360_App = QtWidgets.QApplication(sys.argv)

    window = readingUI()
    controller = UIController(window)
    window.show()

    sys.exit(DXL360_App.exec())

    main()
