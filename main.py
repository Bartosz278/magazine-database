import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter as tk


x = open("data.txt" , "r")
def dataShow():
    for line in x:
        print(line.split("|"))
def addWindow():
    tk.Tk


mainWindow = Tk(className='Data')
# mainWindow.state("zoomed")   <<<<<------ window size
mainWindow.geometry("700x500")

addItem = Button(mainWindow, text = 'Add item', command=addWindow)
addItem.grid(row=0,column=0)

Label(mainWindow, text='First Name').grid(row=0, column=1)
addItem = Entry(mainWindow, width=50)
addItem.grid(row=0, column=1)




mainWindow.mainloop()



