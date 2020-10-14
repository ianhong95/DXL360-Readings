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
        self.setFixedSize(400, 300)
        self.setGeometry(300, 200, 0, 0)
        self._centralWidget = QWidget(self)

        self.layout = QGridLayout()

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.layout)

        self.createInputLayout()
        self.createReadButton()
        # self.signals()
        

    def createInputLayout(self):

        # ----- Initialize input layout ----- #

        self._inputLayout = QGridLayout()
        # self._inputLayout.setGeometry(QRect(QPoint(0, 0), QSize(50,50)))
        self._inputLayout.width = 100
        self._inputLayout.height = 100


        # ----- Assign elements to variables so we can access them later ----- #

        lbCOMPort = QLabel('COM Port:')
        lbDate = QLabel('Date: ')
        lbFilePath = QLabel('Output file path:')
        lbFileName = QLabel('Output file name:')

        edCOMPort = QLineEdit()
        edDate = QLineEdit(
            str(datetime.now().strftime('%b')) +
            '. ' +
            str(datetime.now().day) +
            ', ' +
            str(datetime.now().year)
            )
        edFilePath = QLineEdit('T:\\Engineering\\Engineering\\Projects')
        edFileName = QLineEdit('readings.xlsx')


        # ----- Initialize input form elements, set default values ----- #

        self._inputLayout.addWidget(lbCOMPort, 0, 0)
        self._inputLayout.addWidget(edCOMPort, 0, 1)

        self._inputLayout.addWidget(QLabel('Date:'), 1, 0)
        self._inputLayout.addWidget(QLineEdit(
            str(datetime.now().strftime('%b')) +
            '. ' +
            str(datetime.now().day) +
            ', ' +
            str(datetime.now().year)
            ),
            1, 1)

        self._inputLayout.addWidget(QLabel('Output file path:'), 2, 0)
        self._inputLayout.addWidget(
            QLineEdit('T:\\Engineering\\Engineering\\Projects'), 2, 1)

        self._inputLayout.addWidget(lbFileName, 3, 0)
        self._inputLayout.addWidget(edFileName, 3, 1)

        edCOMPort.setCursorPosition(5)


        # ----- Insert layouts into appropriate spots ----- #

        self.layout.addLayout(self._inputLayout, 0, 0)


    def createReadButton(self):
        
        self.readButton = QPushButton('Take reading')
        self.readButton.setFont((QFont('Calibri', 24)))
        self.readButton.setFixedSize(300, 100)
        self.readButton.hasFocus()

        self.layout.addWidget(self.readButton, 1, 0)

        self.layout.itemAtPosition(1, 0).setAlignment(Qt.AlignCenter)


    def signals(self):
        pass

class readingController:
    pass

    
def main():

    DXL360App = QApplication(sys.argv)

    readingWindow = readingUI()
    readingWindow.show()

    sys.exit(DXL360App.exec_())


if __name__ == '__main__':
    main()