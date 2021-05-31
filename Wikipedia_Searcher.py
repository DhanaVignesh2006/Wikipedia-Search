"""import main

main.Window()

import PyPDF2

# creating a pdf file object
pdfFileObj = open('Class IX physics material 8 Exercises in Motion.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()"""

import subprocess
from tkinter import *

root = Tk()
r = subprocess.call("pip install wikipedia")
lbl = Label(root, text = r)
lbl.pack()
root.mainloop()