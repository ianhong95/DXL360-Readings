import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout

from SerialObjClass import SerialObj as cereal

class readingUI(QMainWindow):

    def __init__(self):

        # Inherit from parent (QMainWindow)
        super().__init__()

        self.defaultPath = 'T:\\Engineering\Enginnering\Projects'

        self.setWindowTitle('DXL360 Readings')
        self.setFixedSize(500, 520)
        self.move(400, 200)
        self._centralWidget = QWidget(self)

        self.layout = QGridLayout()

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.layout)

        self.curRow = 0

        # Initialize UI elements
        self.createInputLayout()
        self.createTable()
        self.createReadButton()
        self.createStartButton()
        self.createClearButton()

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
        self.edFilePath = QLineEdit('T:\\Engineering\\Engineering\\Projects')
        self.edFileName = QLineEdit('readings.xlsx')


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
            '+45°', '+40°', '+30°', '+15°', '0°',
            '-15°', '-30°', '-45°', '-60°', '-75°'
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
        self.startButton.setFixedHeight(50)
        self.startButton.setFont(QFont('Calibri', 16))


    def createClearButton(self):
        self.clearButton = QPushButton('Clear')
        self.clearButton.setFixedHeight(50)
        self.clearButton.setFont(QFont('Calibri', 16))


    def createReadButton(self):
        self.readButton = QPushButton('Take reading')
        self.readButton.setFont((QFont('Calibri', 24)))
        self.readButton.setFixedSize(200, 100)

    
    def layoutElements(self):
        self.layout.addLayout(self._inputLayout, 0, 0)

        # --- Layout start/clear buttons --- #
        self.vertLayout1 = QVBoxLayout()

        self.vertLayout1.addWidget(self.startButton, 0)
        self.vertLayout1.itemAt(0).setAlignment(Qt.AlignRight)

        self.vertLayout1.addWidget(self.clearButton, 1)
        self.vertLayout1.itemAt(1).setAlignment(Qt.AlignRight)

        self.layout.addLayout(self.vertLayout1, 0, 1)
        # ----------------------------------- #

        self.layout.addWidget(self.readingTbl, 3, 0)
        self.layout.itemAtPosition(3,0).setGeometry(QRect(0, 0, 50, 50))

        self.layout.addWidget(self.readButton, 3, 1, 1, 2)
        self.layout.itemAtPosition(3, 0).setAlignment(Qt.AlignHCenter)


    # ----- Define some methods ----- #

    def clearInputs(self):
        # self.edCOMPort.setText('')
        # self.edDate.setText('')
        # self.edArmID.setText('')
        # self.edFilePath.setText('')
        # self.edFileName.setText('')
        
        for row in range(self.readingTbl.rowCount()):
            self.readingTbl.setItem(row, 1, QTableWidgetItem(''))
            self.curRow = 0
            self.readingTbl.setCurrentCell(0, 1)


    def isReading(self):
        if self.startButton.text() == 'Start':
            self.COMPort = 'COM' + self.edCOMPort.text()
            self.startButton.setText('Stop')
        elif self.startButton.text() == 'Stop':
            self.startButton.setText('Start')


    def takeReading(self):
        if self.readingTbl.currentRow() == -1:
            self.readingTbl.setCurrentCell(0, 1)
            self.readingTbl.setItem(self.readingTbl.currentRow(), 1, QTableWidgetItem('success'))
            self.readingTbl.setCurrentCell(self.readingTbl.currentRow() + 1, 1)
        else:
            self.readingTbl.setItem(self.readingTbl.currentRow(), 1, QTableWidgetItem('success'))
            self.readingTbl.setCurrentCell(self.readingTbl.currentRow() + 1, 1)

        print('current row is ' + str(self.readingTbl.currentRow()))


class UIController:
    def __init__(self, readingWindow):
        self.readingWindow = readingWindow
        self.connectSignals()


    def connectSignals(self):
        self.readingWindow.clearButton.clicked.connect(self.readingWindow.clearInputs)
        self.readingWindow.startButton.clicked.connect(self.readingWindow.isReading)
        self.readingWindow.readButton.clicked.connect(self.readingWindow.takeReading)

    
def main():

    DXL360App = QApplication(sys.argv)

    readingWindow = readingUI()
    readingWindow.show()

    UIController(readingWindow=readingWindow)

    sys.exit(DXL360App.exec_())


if __name__ == '__main__':
    main()