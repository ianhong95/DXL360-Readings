# DXL360-Readings

## Overview
At work, the QC team frequently uses a DXL360 digital inclinometer to ensure that devices mounted into our products are level with the ground. The standard procedure is to take a measurement, record it on a sheet of paper, rinse and repeat at different positions.  
  
There's gotta be a better way! I was intrigued by the USB port on the inclinometer that was previously only used for charging, and began experimenting during my lunch breaks.

This is a desktop GUI to read serial output from a DXL360 digital inclinometer, decode the raw bytes into a string, and record it in a pre-defined Microsoft Excel template.
When the program is run, all the buttons except the "Start" button are disabled to prevent errors due to lack of data. When the "Start" button is pressed, the Excel file initializes and creates a new sheet, and it triggers a signal to the other buttons to enable them. Data can be exported to a .xlsx file in the newly created sheet, and the document will automatically save after the data has been entered.  

If fewer than 10 readings are necessary, simply delete the extra values in the left column of the table.  
  
COM port number must be manually entered, and other variables (output file path, name, etc) can be customized.  

## Hardware
- ### DXL360 digital inclinometer
- ### RS232 converter
Since typical computer USB ports are not capable of serial communication, a converter is needed to enable interfacing with the inclinometer using the RS232 protocol. Unfortunately, the USB port on the inclinometer is a mini USB, and a serial adapter with such a connector seems to be fairly rare. To get around this, I dug through my heaps of old cables for a USB type-A to mini USB cable (with data wire) and spliced the mini USB end onto an RS232 adapter. It may not look pretty, but it works!
