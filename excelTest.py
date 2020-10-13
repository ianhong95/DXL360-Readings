import openpyxl
from pynput import keyboard


def on_press(key):

    rowRange = (5, 10)
    entryCol = "C"

    # testCell = worksheet.cell(row=1, column=1)
    # testCell.value = "test"

    for row in range(rowRange[0], rowRange[1]):

        workingCell = worksheet[entryCol + str(row)]

        if workingCell.value is None:
            workingCell.value = str(key)
            print(workingCell.row)
            break

    workbook.save(fileName)


def on_release(key):
    print("You pressed {0}".format(key))

    # ----- Insert data into selected worksheet ----- #


def main():
    pass

if __name__ == "__main__":

    # ----- Enter workbook and worksheet names ----- #
    fileName = "readings.xlsx"
    sheetName = "Sheet1"


    # ----- Load workbook and select worksheet ------ #
    workbook = openpyxl.load_workbook(fileName)
    worksheet = workbook[sheetName]

    # ----- Initialize keyboard listener ----- #
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    while(True):
        main()