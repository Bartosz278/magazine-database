from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from win32api import GetSystemMetrics
# import ttkbootstrap

screenHeight =  int(GetSystemMetrics(0)-GetSystemMetrics(0)*0.10)
screenWidth =  int(GetSystemMetrics(1)-GetSystemMetrics(1)*0.4)


x = open("baza.txt", "r")
def dataShow():
    for line in x:
        table = []
        table = line.split("|")
        listBox.insert('', 'end', values=table)
def dataGain():
    item = searchbar.get()
def addWindow():
    win = tk.Tk()
    win.geometry('700x400')
    frame = Frame(win, padding=20)
    frame.grid(row=1, column=3)
    idLabel = ttk.Label(frame, text='ID').grid(row=0, column=0)
    id1 = ttk.Entry(frame).grid(row=1, column=0)
    nameLabel = ttk.Label(frame, text='Name').grid(row=0, column=1)
    name = ttk.Entry(frame).grid(row=1, column=1)
    typeLabel = ttk.Label(frame, text='Type').grid(row=0, column=2)
    type = ttk.Entry(frame).grid(row=1, column=2)
    cecqLabel = ttk.Label(frame, text='Cecq').grid(row=0, column=3)
    cecq = ttk.Entry(frame).grid(row=1, column=3)
    dateLabel = ttk.Label(frame, text='Date').grid(row=0, column=4)
    date = ttk.Entry(frame).grid(row=1, column=4)


# MAIN WINDOW SIZE ETC.
content = Tk(className='Data')
# content.state("zoomed")
content.geometry(str(screenHeight)+'x'+str(screenWidth))
content.configure(bg="white")

content = Frame(content)
content.pack()

add = Button(content, text='Add item', command=addWindow)
add.grid(row=0, column=0)

Label(content, text='Add item').grid(row=0, column=1)
searchButton = Button(content, text='pokaz - dataShow def ', command=dataShow)
searchButton.grid(row=0, column=4, padx=30, pady=30)
searchbar = Entry(content, width=50)
searchbar.grid(row=0, column=1)
searchtype = StringVar(content)
searchtype.set("name")

type = OptionMenu(content, searchtype, "name", "name", "type", "cecq", "qr", "location", "position", "edition date")
type.grid(row=0, column=2)

search = Button(content, text='Search - dataGain def', command=dataGain)
search.grid(row=0, column=3)

cols = ('ID', 'type', 'CECQ code', 'qr code', 'location', 'placement', 'description', 'edition date')
listBox = Treeview(content, columns=cols, show='headings')
listBox.grid(row=1, column=0, columnspan=8)
listBox.column('ID',width=70,anchor=CENTER)
listBox.column('edition date',width=100)

#ANCHOR=CENTER   <-----------    centrowanie 

for col in cols:
    listBox.heading(col, text=col)
dataShow()

content.mainloop()
