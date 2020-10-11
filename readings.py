import serial
import re
from pynput import keyboard
import csv

# --- CODE FLOW --- #

# 1) Take reading, convert to string [DONE]
# 2) Use RegEx to find a readable portion [DONE]
# 3) Convert readable portion to an actual reading [DONE]
# 4) Make a class for the serial object

# ----------------- #

def on_press(key):
    device.reset_input_buffer()
    if key == keyboard.Key.ctrl_l:
        print(translate())
    print("You pressed {0}".format(key))


def on_release(key):
    print("You released {0}".format(key))


def takeReading():
    rawBytes = device.read(24)
    # print(rawBytes)

    try:
        byteToStr = rawBytes.decode("utf-8")
    except:
        print("Could not decode")
        rawBytes = device.read(24)
        byteToStr = rawBytes.decode("utf-8")
        

    readingRegEx = re.compile(r'(X)(\+|\-)(\d\d)(\d\d)')
    matchObj = readingRegEx.search(byteToStr)

    if matchObj != None:
        return matchObj.groups()


def reverseSign(readingSign):
    if readingSign == "+":
        sign = "-"
    elif readingSign == "-":
        sign = "+"
    
    return sign


def translate():
    reading = takeReading()

    # Need to reverse sign convention
    try:
        realSign = reverseSign(reading[1])
    except:
        print("Reading glitched")
        reading = takeReading()
        realSign = reverseSign(reading[1])

    # Translate the numerical portion by adding whole and decimal
    whole = int(reading[2])
    dec = round(int(reading[3])/100, 1)     # Change this line to change rounding

    trnslReading = whole + dec

    finalTrnsl = realSign + str(trnslReading)

    return [realSign, trnslReading, finalTrnsl]


def main():
    # angle = translate()
    # print(angle[2])
    pass
    

if __name__ == "__main__":

    device = serial.Serial(port='COM5', baudrate=9600)
    print(device.portstr)

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    
    while(True):
        main()