from readingUI import readingUI, internalController
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
import serial

from SerialObjClass import SerialObj as cereal


def takeReading(device):

    rawBytes = device.serialRead()
    reading = device.translate()

    print(device.finalReading)

    return reading


def recordReading(mainGUI, device):

    print('current row is ' + str(mainGUI.readingTbl.currentRow()))

    reading = takeReading(device)

    if mainGUI.readingTbl.currentRow() == -1:
        mainGUI.readingTbl.setCurrentCell(0, 1)
        mainGUI.readingTbl.setItem(mainGUI.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        mainGUI.readingTbl.setCurrentCell(mainGUI.readingTbl.currentRow() + 1, 1)

    elif mainGUI.readingTbl.currentRow() != -1 and mainGUI.readingTbl.currentRow() < mainGUI.readingTbl.rowCount() - 1:
        mainGUI.readingTbl.setItem(mainGUI.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        mainGUI.readingTbl.setCurrentCell(mainGUI.readingTbl.currentRow() + 1, 1)

    elif mainGUI.readingTbl.currentRow() != -1 and mainGUI.readingTbl.currentRow() == mainGUI.readingTbl.rowCount() - 1:
        mainGUI.readingTbl.setItem(mainGUI.readingTbl.currentRow(), 1, QTableWidgetItem(reading[2]))
        print('you\'re done!')

    print('now the current row is ' + str(mainGUI.readingTbl.currentRow()))

class externalController:
    def __init__(self, mainGUI):
        self.mainGUI = mainGUI
        self.COMPort = 'COM' + mainGUI.edCOMPort.text()
        self.connectExtSigs()
    
    
    def initCOMPort(self, Port):
        self.serialDevice = cereal(Port, 9600)


    def connectExtSigs(self):
        self.mainGUI.readButton.clicked.connect(lambda: recordReading(self.mainGUI, self.serialDevice))
        self.mainGUI.startButton.clicked.connect(lambda: self.initCOMPort(self.COMPort))


def main():
    DXL360_App = QtWidgets.QApplication(sys.argv)

    mainGUI = readingUI()

    intController = internalController(mainGUI)
    extController = externalController(mainGUI)

    mainGUI.show()

    sys.exit(DXL360_App.exec())


if __name__ == '__main__':
    main()
