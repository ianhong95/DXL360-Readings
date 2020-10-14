import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout

class readingUI(QMainWindow):

    def __init__(self):

        # Inherit from parent (QMainWindow)
        super().__init__()

        self.defaultPath = 'T:\\Engineering\Enginnering\Projects'

        self.setWindowTitle('DXL360 Readings')
        self.setFixedSize(600, 500)
        self.move(400, 200)
        self._centralWidget = QWidget(self)

        self.layout = QGridLayout()

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.layout)

        self.createInputLayout()
        self.createReadButton()
        self.createStartButton()
        self.createClearButton()
        

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
        self.lbCOMPort.setAlignment(Qt.AlignRight)
        self.lbDate.setAlignment(Qt.AlignRight)
        self.lbArmID.setAlignment(Qt.AlignRight)
        self.lbFilePath.setAlignment(Qt.AlignRight)
        self.lbFileName.setAlignment(Qt.AlignRight)

        self.edCOMPort.setFixedWidth(100)
        self.edCOMPort.setAlignment(Qt.AlignTop)

        self.edDate.setFixedWidth(200)
        self.edDate.setAlignment(Qt.AlignTop)

        self.edArmID.setFixedWidth(200)
        self.edArmID.setAlignment(Qt.AlignTop)
        self.edArmID.setCursorPosition(0)

        self.edFilePath.setFixedWidth(200)
        self.edFilePath.setAlignment(Qt.AlignTop)
        self.edFilePath.setCursorPosition(0)
        
        self.edFileName.setFixedWidth(200)
        self.edFileName.setAlignment(Qt.AlignTop)


        # ----- Insert layouts into appropriate spots ----- #

        self.layout.addLayout(self._inputLayout, 0, 0)


    # ----- Create some buttons ----- #

    def createStartButton(self):
        self.startButton = QPushButton('Start')

        self.layout.addWidget(self.startButton, 1, 0)
        self.layout.itemAtPosition(1, 0).setAlignment(Qt.AlignRight)


    def createClearButton(self):
        self.clearButton = QPushButton('Clear')

        self.layout.addWidget(self.clearButton, 1, 1)
        self.layout.itemAtPosition(1, 1).setAlignment(Qt.AlignLeft)


    def createReadButton(self):
        
        self.readButton = QPushButton('Take reading')
        self.readButton.setFont((QFont('Calibri', 24)))
        self.readButton.setFixedSize(400, 100)
        self.readButton.hasFocus()

        self.layout.addWidget(self.readButton, 2, 0, 1, 2)

        self.layout.itemAtPosition(2, 0).setAlignment(Qt.AlignHCenter)


    # ----- Define some methods ----- #

    def clearInputs(self):
        self.edCOMPort.setText('')
        self.edDate.setText('')
        self.edArmID.setText('')
        self.edFilePath.setText('')
        self.edFileName.setText('')

    def isReading(self):
        if self.startButton.text() == 'Start':
            self.startButton.setText('Stop')
        elif self.startButton.text() == 'Stop':
            self.startButton.setText('Start')

    def takeReading(self):
        pass


class UIController:
    def __init__(self, readingWindow):
        self.readingWindow = readingWindow
        self.connectSignals()


    def connectSignals(self):
        self.readingWindow.clearButton.clicked.connect(self.readingWindow.clearInputs)
        self.readingWindow.startButton.clicked.connect(self.readingWindow.isReading)

    
def main():

    DXL360App = QApplication(sys.argv)

    readingWindow = readingUI()
    readingWindow.show()

    UIController(readingWindow=readingWindow)

    sys.exit(DXL360App.exec_())


if __name__ == '__main__':
    main()