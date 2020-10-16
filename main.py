from readingUI import UIController, readingUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
import serial

from SerialObjClass import SerialObj as cereal


def takeReading():
    rawBytes = serialDevice.serialRead()
    reading = serialDevice.translate()

    print(serialDevice.finalReading)

    return reading


def recordReading(window):
    print('current row is ' + str(window.readingTbl.currentRow()))

    reading = takeReading()

    if window.readingTbl.currentRow() == -1:
        window.readingTbl.setCurrentCell(0, 1)
        window.readingTbl.setItem(window.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        window.readingTbl.setCurrentCell(window.readingTbl.currentRow() + 1, 1)

    elif window.readingTbl.currentRow() != -1 and window.readingTbl.currentRow() < window.readingTbl.rowCount() - 1:
        window.readingTbl.setItem(window.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        window.readingTbl.setCurrentCell(window.readingTbl.currentRow() + 1, 1)

    elif window.readingTbl.currentRow() != -1 and window.readingTbl.currentRow() == window.readingTbl.rowCount() - 1:
        window.readingTbl.setItem(window.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        print('you\'re done!')

    print('now the current row is ' + str(window.readingTbl.currentRow()))


def main():
    pass


if __name__ == '__main__':

    DXL360_App = QtWidgets.QApplication(sys.argv)

    window = readingUI()
    controller = UIController(window)

    serialDevice = cereal('COM6', 9600)

    window.readButton.clicked.connect(lambda: recordReading(window))


    window.show()

    sys.exit(DXL360_App.exec())

    main()
