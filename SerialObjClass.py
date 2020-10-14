import serial


class SerialObj:
    def __init__(self, COMPort, baudRate=9600):
        self.COMPort = COMPort
        self.baudRate = baudRate

        self.serialDevice = serial.Serial(self.COMPort, self.baudRate)

    
    def serialRead(self):
        self.rawBytes = self.serialDevice.read(24)

        return self.rawBytes


    def decodeBytes(self, rawBytes):
        try:
            self.byteToStr = rawBytes.decode('utf-8')
            self.decodeable = True
            return self.byteToStr
        except:
            self.decodeable = False


    def regExMatching(self, byteToStr):

        regExPattern = re.compile(r'(X)(+|-)(\d\d)(\d\d)')
        
        self.matchObj = regExPattern.search(byteToStr)

        if matchObj != None:
            return self.matchObj.groups()
        else:
            print('No match found, processing next string of bytes')

    
    def reverseSign(self, readingSign):
        if readingSign == '+':
            readingSign = '-'
        elif readingSign == '-':
            readingSign = '+'

        return readingSign


    def translate(self):
        while self.decodeable is not True:
            self.rawBytes = self.serialRead()
            self.byteToStr = self.decodeBytes(self.rawBytes)

        self.readingGrps = self.regExMatching(self.byteToStr)

        self.readingSign = reverseSign(self.readingGrps[1])
        self.whole = int(self.readingGrps[2])
        self.dec = round(int(self.readingGrps[3]/100), 1)

        self.numReading = self.whole + self.dec

        self.finalReading = self.readingSign + str(self.numReading)

        return [self.readingSign, self.numReading, self.finalReading]