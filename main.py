from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
# from win32api import GetSystemMetrics
import datetime
import ttkbootstrap

# screenHeight = int(GetSystemMetrics(0) - GetSystemMetrics(0) * 0.10)
# screenWidth = int(GetSystemMetrics(1) - GetSystemMetrics(1) * 0.4)

def refresh():
    with open('baza.txt') as reader, open('baza.txt', 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()
    x = open('baza.txt','r')
    for row in listBox.get_children():
        listBox.delete(row)
    for line in x:
        table = []
        table = line.split("|")
        table.insert(9,'O')
        listBox.insert('', 'end', values=table)
    x.close()

def dataGain():
    x = open("baza.txt", "r")
    item = searchbar.get()


def addWindow():
    xr = open("baza.txt", "r")

    def addData():
        empty_line = ""
        xa = open("baza.txt", "a")
        new_item.append(type.get())
        new_item.append(name.get())
        new_item.append(cecq.get())
        new_item.append(qr.get())
        new_item.append(location.get())
        new_item.append(placement.get())
        new_item.append(description.get())
        new_item.append(str(datetime.date.today()))
        print(new_item)
        i = 0
        for i in range(1, 8):
            empty_line += new_item[i]
        if empty_line:
            xa.write('\n')
            for item in new_item:
                xa.write(str(item) + "|")
                i += 1


        xa.close()
        refresh()
        win.destroy()
        addWindow()

    win = Tk(className='Add new item')
    frame = Frame(win, padding=20)
    frame.grid(row=1, column=3)

    new_item = []
    last_line = ""
    for line in xr:
        pass
        last_line = line
    new_item.append(int(last_line.split("|")[0]) + 1)

    typeLabel = ttk.Label(frame, text='Type').grid(row=0, column=1)
    type = ttk.Entry(frame)
    type.grid(row=1, column=1)
    nameLabel = ttk.Label(frame, text='Name').grid(row=0, column=2)
    name = ttk.Entry(frame)
    name.grid(row=1, column=2)
    cecqLabel = ttk.Label(frame, text='Cecq').grid(row=0, column=3)
    cecq = ttk.Entry(frame)
    cecq.grid(row=1, column=3)
    qrLabel = ttk.Label(frame, text='qr').grid(row=0, column=4)
    qr = ttk.Entry(frame)
    qr.grid(row=1, column=4)
    locationLabel = ttk.Label(frame, text='location').grid(row=0, column=5)
    location = ttk.Entry(frame)
    location.grid(row=1, column=5)
    placementLabel = ttk.Label(frame, text='placement').grid(row=0, column=6)
    placement = ttk.Entry(frame)
    placement.grid(row=1, column=6)
    descriptionLabel = ttk.Label(frame, text='description').grid(row=0, column=7)
    description = ttk.Entry(frame)
    description.grid(row=1, column=7)

    addRecordButton = tk.Button(frame, text="create", command=addData, font='Calibri 14')
    addRecordButton.grid(row=1, column=8, padx=20,ipady=4)

# MAIN WINDOW SIZE ETC.
root = Tk(className='Data')
# content.state("zoomed")
# content.geometry(str(screenHeight) + 'x' + str(screenWidth))
root.config(bg='#EFF9FF')

content = Frame(root)
content.pack()
# content.grid(row=0,column=0)

addButton = tk.Button(content,text='Add item', command=addWindow, font='Calibri 14')
addButton.grid(row=0, column=0,ipady=4)

Label(content, text='Add item').grid(row=0, column=2)
searchButton = tk.Button(content, text='pokaz-dataShow def ',command=refresh, font='Calibri 14')
searchButton.grid(row=0, column=4, padx=30, pady=30,ipady=4)
searchbar = Entry(content, width=50)
searchbar.grid(row=0, column=1,ipady=3)

searchtype = StringVar(content)
searchtype.set("name")
type = OptionMenu(content, searchtype, "name", "name", "type", "cecq", "qr", "location", "position", "edition date")
type.grid(row=0, column=2,ipady=8)

search = tk.Button(content, text='Search - dataGain def', font='Calibri 14', command=dataGain)
search.grid(row=0, column=3,ipady=4)

                     #MAIN LIST

columns = ('ID', 'type','name', 'CECQ code', 'qr code', 'location', 'placement', 'description', 'edition date', 'CheckBox')
listBox = Treeview(content, columns=columns, show='headings')
listBox.grid(row=1, column=0, columnspan=9)

rowHeight = ttk.Style()
rowHeight.configure('Treeview', rowheight=30)

for col in columns:
    listBox.heading(col, text=col)
<<<<<<< Updated upstream
    listBox.column(col,anchor=CENTER)
=======
    listBox.column(col, anchor=CENTER)

def changeColumnWidth(size, *args):
    for i in args:
        listBox.column(i, width=size)

counter = 0
def prt(event):
    print(counter)

listBox.bind('<Double-Button-1>', prt)

changeColumnWidth(60, 'ID', 'QR code', 'Check')
changeColumnWidth(150, 'type', 'edition date', 'placement')

>>>>>>> Stashed changes
refresh()

content.mainloop()
