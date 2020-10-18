from readingUI import readingUI, internalController
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
import serial

import openpyxl as xl

from SerialObjClass import SerialObj as cereal


def takeReading(device):

    rawBytes = device.serialRead()
    reading = device.translate()

    print(device.finalReading)

    return reading


def recordReading(mainGUI, device):
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


class xlWorkbook:
    def __init__(self, filePath, fileName):
        self.filePath = filePath
        self.fileName = fileName
        self.xlWb = self.initWorkbook()
    

    def initWorkbook(self):
        self.xlWb = xl.load_workbook(self.filePath + '\\' + self.fileName)
        return self.xlWb
        

class externalController:
    def __init__(self, mainGUI):
        self.mainGUI = mainGUI

        self.connectExtSigs()
    
    
    def initCOMPort(self):
        if self.mainGUI.startButton.text() == 'Stop':
            self.COMPort = 'COM' + self.mainGUI.edCOMPort.text()
            try:
                self.serialDevice = cereal(self.COMPort, 9600)
            except:
                print('Try again!')


    # ---- Excel handling functions ----- #
    def xlWb(self):
        self.xlPath = self.mainGUI.edFilePath.text()
        self.xlFile = self.mainGUI.edFileName.text() + '.xlsx'

        # Initialize excel workbook object
        wbObject = xlWorkbook(self.xlPath, self.xlFile)
        self.wb = wbObject.initWorkbook()
        self.workSheet = self.wb['Sheet1']


    def xlWrite(self):

        dateCell = self.workSheet['C2']
        armIDCell = self.workSheet['C3']
        armDescription = self.workSheet['C4']

        dateCell.value = self.mainGUI.edDate.text()
        armIDCell.value = self.mainGUI.edArmID.text()

        tblRowCount = self.mainGUI.readingTbl.rowCount()
        for row in range(tblRowCount):
            try:
                dataValue = self.mainGUI.readingTbl.item(row, 1).text()
                dataCell = self.workSheet['C' + str(row + 6)]
                print('current row: ' + str(dataCell.row))
                dataCell.value = str(dataValue)
            except:
                print('no data!')

        self.wb.save(self.xlPath + '\\' + self.xlFile)
        print('Data exported!')


    def connectExtSigs(self):
        self.mainGUI.readButton.clicked.connect(lambda: recordReading(self.mainGUI, self.serialDevice))
        self.mainGUI.startButton.clicked.connect(self.initCOMPort)
        self.mainGUI.startButton.clicked.connect(self.xlWb)
        self.mainGUI.exportButton.clicked.connect(self.xlWrite)


def main():
    DXL360_App = QtWidgets.QApplication(sys.argv)

    mainGUI = readingUI()

    intController = internalController(mainGUI)
    extController = externalController(mainGUI)

    mainGUI.show()

    sys.exit(DXL360_App.exec())


if __name__ == '__main__':
    main()