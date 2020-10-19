# DXL360-Readings
Read serial output from a DXL360 digital level and record it in Microsoft Excel using a pre-defined template.  
  
When the program is run, all the buttons except the "Start" button are disabled to prevent errors due to lack of data. When the "Start" button is pressed, the Excel file initializes and creates a new sheet, and it triggers a signal to the other buttons to enable them. Data can be exported to a .xlsx file in the newly created sheet, and the document will automatically save after the data has been entered.  

If fewer than 10 readings are necessary, simply delete the extra values in the left column of the table.  
  
COM port number must be manually entered, and other variables (output file path, name, etc) can be customized.  