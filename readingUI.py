import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGridLayout

class readingUI(QMainWindow):

    def __init__(self):

        # Inherit from parent (QMainWindow)
        super().__init__()

        self.defaultPath = 'T:\\Engineering\Enginnering\Projects'

        self.setWindowTitle('DXL360 Readings')
        self.setGeometry(200, 200, 500, 300)
        self._centralWidget = QWidget(self)

        self.layout = QGridLayout()

        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.layout)

        self.createInputLayout()
        self.createReadButton()
        

    def createInputLayout(self):

        self._inputLayout = QVBoxLayout()

        self._inputFrm = QFormLayout()
        self._inputFrm.setGeometry(QRect(0, 0, 50, 50))
        self._inputFrm.setFieldGrowthPolicy(False)
        self._inputFrm.addRow('COM Port:', QLineEdit())
        self._inputFrm.addRow('Date:', QLineEdit())
        self._inputFrm.addRow('Output to file path:', QLineEdit(self.defaultPath))

        self._inputLayout.setGeometry(QRect(0, 0, 100,100))
        self._inputLayout.addLayout(self._inputFrm)
        # self._centralWidget.setLayout(self._inputLayout)
        self.layout.addLayout(self._inputLayout, 0, 0)

        # Example of how to get text from inputFrm:
            # widget_item = self._inputFrm.itemAt(0)
            # text = widget_item.widget().text()
            # print(text)


    def createReadButton(self):
        
        self.readButton = QPushButton('Take reading')
        self.readButton.setGeometry(0, 500, 50, 100)

        self._btnLayout.addWidget(self.readButton)

        self.layout.addWidget(self.readButton, 0, 1)

    
def main():

    DXL360App = QApplication(sys.argv)

    readingWindow = readingUI()
    readingWindow.show()

    sys.exit(DXL360App.exec_())


if __name__ == '__main__':
    main()