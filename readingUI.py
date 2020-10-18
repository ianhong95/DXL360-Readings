import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout

from SerialObjClass import SerialObj as cereal

class readingUI(QMainWindow):

    def __init__(self):

        # Inherit from parent (QMainWindow)
        super().__init__()

        self.defaultPath = 'T:\\Engineering\\Enginnering\\Projects'

        self.setWindowTitle('DXL360 Readings')
        self.setFixedSize(800, 1000)
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

        # Place UI elements into grid slots
        self.layoutElements()


    def createInputLayout(self):

        # ----- Initialize input layout ----- #

        self._inputLayout = QGridLayout()


        # ----- Assign elements to variables so we can access them later ----- #

        self.lbCOMPort = QLabel('COM Port:')
        self.lbDate = QLabel('Date:')
        self.lbArmID = QLabel('Arm ID:')
        self.lbFilePath = QLabel('Output file path:')
        self.lbFileName = QLabel('Output file name:')

        self.edCOMPort = QLineEdit()
        self.edDate = QLineEdit(
            str(datetime.now().strftime('%b')) +
            '. ' +
            str(datetime.now().day) +
            ', ' +
            str(datetime.now().year)
            )
        self.edArmID = QLineEdit(str(datetime.now()))
        self.edFilePath = QLineEdit('C:\\Users\\ianho\\Dropbox\\Excel Documents')
        self.edFileName = QLineEdit('readings')


        # ----- Initialize input form elements, set default values ----- #

        self._inputLayout.addWidget(self.lbCOMPort, 0, 0)
        self._inputLayout.addWidget(self.edCOMPort, 0, 1)

        self._inputLayout.addWidget(self.lbDate, 1, 0)
        self._inputLayout.addWidget(self.edDate, 1, 1)

        self._inputLayout.addWidget(self.lbArmID, 2, 0)
        self._inputLayout.addWidget(self.edArmID, 2, 1)

        self._inputLayout.addWidget(self.lbFilePath, 3, 0)
        self._inputLayout.addWidget(self.edFilePath, 3, 1)

        self._inputLayout.addWidget(self.lbFileName, 4, 0)
        self._inputLayout.addWidget(self.edFileName, 4, 1)

        # ----- Format input form elements ----- #

        for row in range(0, 5):
            self._inputLayout.itemAtPosition(row, 0).setAlignment(Qt.AlignLeft)     
            self._inputLayout.itemAtPosition(row, 1).setAlignment(Qt.AlignLeft)

        self.edArmID.setCursorPosition(0)
        self.edFilePath.setCursorPosition(0)

        self.edFilePath.setToolTip(self.edFilePath.text())

    
    def createTable(self):
        self.defaultArmPos = [
            '+45', '+40', '+30', '+15', '0',
            '-15', '-30', '-45', '-60', '-75'
        ]

        self.readingTbl = QTableWidget(len(self.defaultArmPos), 2)

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

        self.layout.addLayout(self.vertLayout1, 0, 1)
        # ----------------------------------- #

        self.layout.addWidget(self.readingTbl, 3, 0)
        self.layout.itemAtPosition(3,0).setGeometry(QRect(0, 0, 50, 50))

        self.layout.addWidget(self.readButton, 3, 1, 1, 2)
        self.layout.itemAtPosition(3, 0).setAlignment(Qt.AlignHCenter)


    # ----- Define some methods ----- #

    def clearInputs(self): 
        for row in range(self.readingTbl.rowCount()):
            self.readingTbl.setItem(row, 1, QTableWidgetItem(''))
        
        self.readingTbl.setCurrentCell(0, 1)


    def isReading(self):
        if self.startButton.text() == 'Start':
            self.readButton.setEnabled(True)
            self.startButton.setText('Stop')
            self.exportButton.setEnabled(True)
        elif self.startButton.text() == 'Stop':
            self.startButton.setText('Start')
            self.readButton.setEnabled(False)
            self.exportButton.setEnabled(False)


class internalController:
    def __init__(self, readingWindow):
        self.readingWindow = readingWindow
        self.connectIntSigs()


    def connectIntSigs(self):
        self.readingWindow.clearButton.clicked.connect(self.readingWindow.clearInputs)
        self.readingWindow.startButton.clicked.connect(self.readingWindow.isReading)