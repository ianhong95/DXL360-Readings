import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5 import QtWidgets

from SerialObjClass import SerialObj as cereal

class readingUI(QMainWindow):

    def __init__(self):

        # Inherit from parent (QMainWindow)
        super().__init__()

        self.defaultPath = 'C:\\Users\\ianho\\Dropbox\\Excel Documents'

        self.setWindowTitle('DXL360 Readings')
        self.setFixedSize(500, 520)
        self.move(400, 200)
        self._centralWidget = QWidget(self)

        self.layout = QGridLayout()

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.layout)

        # Initialize UI elements
        self.createInputLayout()
        self.createTable()
        self.createReadButton()
        self.createStartButton()
        self.createClearButton()
        self.createExportButton()
        self.createStatusLabel()

        # Place UI elements into grid slots
        self.layoutElements()


    def createInputLayout(self):

        # ----- Initialize input layout ----- #

        self._inputLayout = QGridLayout()

        # ----- Assign elements to variables so we can access them later ----- #
        self.labels = {}
        labels = {
            'lbCOMPort': 'COM Port:',
            'lbDate': 'Date:',
            'lbArmID': 'Arm ID:',
            'lbArmDesc': 'Arm Description:',
            'lbFilePath': 'Output file path:',
            'lbFileName': 'Output file name:' 
        }

        self.lineEdits = {}
        lineEdits = {
            'edCOMPort': '3',
            'edDate': str(datetime.now().strftime('%b')) + '. ' +
                str(datetime.now().day) + ', ' +
                str(datetime.now().year),
            'edArmID': str(datetime.now().strftime('%I%M%S')),
            'edArmDesc': '',
            'edFilePath': self.defaultPath,
            'edFileName': 'readings'       
        }

        # ----- Initialize input form elements, set default values ----- #
        for labelName, labelText in labels.items():
            self.labels[labelName] = QLabel(labelText)

        for lineEditName, lineEditText in lineEdits.items():
            self.lineEdits[lineEditName] = QLineEdit(lineEditText)

        labelKeys = list(self.labels.keys())
        lineEditKeys = list(self.lineEdits.keys())

        for row in range(len(labels)):
            self._inputLayout.addWidget(self.labels[labelKeys[row]], row, 0)
            self._inputLayout.addWidget(self.lineEdits[lineEditKeys[row]], row, 1)

        # ----- Format input form elements ----- #

        for row in range(len(self.labels)):
            self._inputLayout.itemAtPosition(row, 0).setAlignment(Qt.AlignLeft)     
            self._inputLayout.itemAtPosition(row, 1).setAlignment(Qt.AlignLeft)

        for lineEdit in self.lineEdits.values():
            lineEdit.setCursorPosition(0)

        self.lineEdits['edFilePath'].setToolTip(self.lineEdits['edFilePath'].text())

    
    def createTable(self):
        self.defaultArmPos = [
            '+45', '+40', '+30', '+15', '0',
            '-15', '-30', '-45', '-60', '-75'
        ]

        self.readingTbl = QTableWidget(len(self.defaultArmPos), 2)
        self.readingTbl.setFixedSize(185, 325)

        self.readingTbl.setHorizontalHeaderLabels(['Arm Position', 'FR5 Angle'])
        
        self.readingTbl.setColumnWidth(0, 80)
        self.readingTbl.setColumnWidth(1, 80)
        

        for row in range(self.readingTbl.rowCount()):
            self.readingTbl.setItem(row, 0, QTableWidgetItem(self.defaultArmPos[row]))

    # ----- Create some buttons ----- #

    def createStartButton(self):
        self.startButton = QPushButton('Start')
        self.startButton.setFixedHeight(30)
        self.startButton.setFont(QFont('Calibri', 16))


    def createClearButton(self):
        self.clearButton = QPushButton('Clear')
        self.clearButton.setFixedHeight(30)
        self.clearButton.setFont(QFont('Calibri', 16))


    def createReadButton(self):
        self.readButton = QPushButton('Take reading')
        self.readButton.setFont(QFont('Calibri', 24))
        self.readButton.setFixedSize(200, 100)
        self.readButton.setEnabled(False)

    
    def createExportButton(self):
        self.exportButton = QPushButton('Export Data')
        self.exportButton.setFixedHeight(30)
        self.exportButton.setFont(QFont('Calibri', 16))
        self.exportButton.setEnabled(False)


    def createStatusLabel(self):
        self.statusLabel = QLabel('Click "Start" to begin!')
        self.statusLabel.setFixedHeight(30)
        self.statusLabel.setFont(QFont('Calibri', 16))
        self.statusLabel.setAlignment(Qt.AlignLeft)

    
    def layoutElements(self):
        self.layout.addLayout(self._inputLayout, 0, 0)

        # --- Layout start/clear buttons --- #
        self.vertLayout1 = QVBoxLayout()

        self.vertLayout1.addWidget(self.startButton, 0)
        self.vertLayout1.itemAt(0).setAlignment(Qt.AlignHCenter)

        self.vertLayout1.addWidget(self.clearButton, 1)
        self.vertLayout1.itemAt(1).setAlignment(Qt.AlignHCenter)

        self.vertLayout1.addWidget(self.exportButton, 2)
        self.vertLayout1.itemAt(2).setAlignment(Qt.AlignHCenter)

        self.layout.addLayout(self.vertLayout1, 1, 0)
        # ----------------------------------- #

        self.layout.addWidget(self.readingTbl, 0, 1, 3, 1)
        self.layout.itemAtPosition(0, 1).setAlignment(Qt.AlignTop)

        self.layout.addWidget(self.readButton, 2, 0)
        self.layout.itemAtPosition(2, 0).setAlignment(Qt.AlignHCenter)

        self.layout.addWidget(self.statusLabel, 2, 1)


    # ----- Define some methods ----- #

    def clearInputs(self): 
        for row in range(self.readingTbl.rowCount()):
            self.readingTbl.setItem(row, 1, QTableWidgetItem(''))
        
        self.readingTbl.setCurrentCell(0, 1)


    def isReading(self):
        if self.startButton.text() == 'Start':
            self.count = 0

            for row in range(self.readingTbl.rowCount()):
                if self.readingTbl.item(row, 0).text() != '':
                    self.count += 1

            self.readButton.setEnabled(True)
            self.startButton.setText('Stop')
            self.exportButton.setEnabled(True)
            self.statusLabel.setText('Ready!')
            
        elif self.startButton.text() == 'Stop':
            self.startButton.setText('Start')
            self.readButton.setEnabled(False)
            self.exportButton.setEnabled(False)
            self.clearButton.setEnabled(False)


class internalController:
    def __init__(self, readingWindow):
        self.readingWindow = readingWindow
        self.connectIntSigs()


    def connectIntSigs(self):
        self.readingWindow.clearButton.clicked.connect(self.readingWindow.clearInputs)
        self.readingWindow.startButton.clicked.connect(self.readingWindow.isReading)
        self.readingWindow.startButton.clicked.connect(self.readingWindow.clearInputs)
        self.readingWindow.exportButton.clicked.connect(self.readingWindow.isReading)


def main():
    test = QtWidgets.QApplication(sys.argv)

    testGUI = readingUI()

    testGUI.show()

    sys.exit(test.exec())


if __name__ == '__main__':
    main()