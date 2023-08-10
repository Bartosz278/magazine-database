import time
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
# from win32api import GetSystemMetrics
import datetime
import ttkbootstrap
import keyboard
from ttkbootstrap.constants import *
import ttkwidgets
import keyboard
import shutil



# screenHeight = int(GetSystemMetrics(0) - GetSystemMetrics(0) * 0.10)
# screenWidth = int(GetSystemMetrics(1) - GetSystemMetrics(1) * 0.4)
def changeColumnWidth(size, *args):
    for i in args:
        listBox.column(i, width=size)

def editRowWindow(event):
    def edit_item():
        id_var = 1
        edit_tab = []
        x = open("baza.txt","r")
        text = x.readlines()
        x = open("baza.txt","w")
        selected = listBox.focus()
        edit_id = listBox.item(selected,'values')[0]
        for row in text:
            if str(id_var) == edit_id:
                add_item = ""
                k = 0
                new_item = []
                new_item.append(id_var)
                new_item.append(typeLabelValue.get())
                new_item.append(nameLabelValue.get())
                new_item.append(cecqLabelValue.get())
                new_item.append(qrLabelValue.get())
                new_item.append(locationLabelValue.get())
                new_item.append(placementLabelValue.get())
                new_item.append(str(datetime.date.today()))
                new_item.append(descriptionLabelValue.get())
                for item in new_item:
                    if k >= 8:
                        add_item += str(item)
                    else:
                        add_item += str(item) + "|"
                    k += 1
                edit_tab.append(add_item)
            else:
                edit_tab.append(row)
            id_var += 1
        for element in edit_tab:
            x.writelines(str(element))
        x.close()
        id_update()
        refresh()

    editWindow = Tk(className='Edit window')
    editFrame = ttk.Frame(editWindow, padding=50)
    editFrame.pack()
    editWindow.geometry("350x350")

    editColumn1 = ttk.Frame(editFrame)
    editColumn1.pack(side=LEFT)
    editColumn2 = ttk.Frame(editFrame)
    editColumn2.pack(side=LEFT)

    selected = listBox.focus()
    x = (listBox.item(selected, 'values'))

    x1 = StringVar(value=x[1])

    typeLabel = Label(editColumn1, text='Type:', font='Calibri 14',anchor='w',width=10).pack()
    typeLabelValue = ttk.Entry(editColumn2, font='Calibri 14',width=20)
    typeLabelValue.insert(END,x[1])
    typeLabelValue.pack()

    nameLabel = ttk.Label(editColumn1, text='Name:', font='Calibri 14',anchor='w',width=10).pack()
    nameLabelValue = ttk.Entry(editColumn2,text=x[2],font='Calibri 14',width=20)
    nameLabelValue.insert(END, x[2])
    nameLabelValue.pack()

    cecqLabel = ttk.Label(editColumn1, text='Cecq:', font='Calibri 14',anchor='w',width=10).pack()
    cecqLabelValue = ttk.Entry(editColumn2, text=x[3], font='Calibri 14',width=20)
    cecqLabelValue.insert(END, x[3])
    cecqLabelValue.pack()

    qrLabel = ttk.Label(editColumn1, text='Qr code:', font='Calibri 14',anchor='w',width=10).pack()
    qrLabelValue = ttk.Entry(editColumn2, text=x[4], font='Calibri 14',width=20)
    qrLabelValue.insert(END, x[4])
    qrLabelValue.pack()

    locationLabel = ttk.Label(editColumn1, text='location:', font='Calibri 14',anchor='w',width=10).pack()
    locationLabelValue = ttk.Entry(editColumn2, text=x[5], font='Calibri 14',width=20)
    locationLabelValue.insert(END, x[5])
    locationLabelValue.pack()

    placementLabel = ttk.Label(editColumn1, text='placement:', font='Calibri 14',anchor='w',width=10).pack()
    placementLabelValue = ttk.Entry(editColumn2, text=x[6], font='Calibri 14',width=20)
    placementLabelValue.insert(END, x[6])
    placementLabelValue.pack()

    descriptionLabel = ttk.Label(editColumn1, text='description:', font='Calibri 14',anchor='w',width=10).pack()
    descriptionLabelValue = ttk.Entry(editColumn2, text=x[8], font='Calibri 14',width=20)
    descriptionLabelValue.insert(END, x[8])
    descriptionLabelValue.pack()


    EditButton = tk.Button(editWindow, text='Edit', font='Calibri 14',command=edit_item).pack(pady=5,ipadx=10)
def refresh():
    with open('baza.txt') as reader, open('baza.txt', 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()
    x = open('baza.txt', 'r')
    for row in listBox.get_children():
        listBox.delete(row)
    for line in x:
        table = []
        table = line.split("|")
        listBox.insert('', 'end', value=table)
    x.close()


def dataGain(item):
    x = open("baza.txt", "r")
    item = searchbar.get()
    item_type = columns.index(searchtype.get())
    for row in listBox.get_children():
        listBox.delete(row)
    for line in x:
        line = line.split("|")
        if item in line[item_type]:
            listBox.insert('', "end", values=line)
    if item.strip():
        pass
    else:
        refresh()
    for line in x:
        line = line.split("|")
        for elem in line:
            index = elem.find(item)
            if index == -1:
                continue
            else:
                listBox.insert('', 'end', values=line)
    x.close()


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
        new_item.append(str(datetime.date.today()))
        new_item.append(description.get())
        k = 0
        for i in range(1, 7):
            empty_line += new_item[i]
        if empty_line:
            xa.writelines('')
            for item in new_item:
                if k==8:
                    xa.writelines(str(item))
                else:
                    xa.writelines(str(item) + "|")
                k += 1

        id_update()
        xa.close()
        xr.close()
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

    addRecordButton = tk.Button(frame, text="create", command=addData, font='Calibri 14').grid(row=1, column=8, padx=20,ipady=4)

def delete_item(event):
    x = open("baza.txt", "w")
    for i in listBox.selection():
        listBox.delete(i)
    for line in listBox.get_children():
        item = []
        k = 0
        for value in listBox.item(line)["values"]:
            if k == 8:
                x.writelines(str(value))
            else:
                x.writelines(str(value) + "|")
            k += 1
    x.close()
    id_update()
    refresh()
def id_update():
    max_rows = 1
    id = 1
    x = open("baza.txt", "r")
    text = x.readlines()
    x = open("baza.txt", "w")
    #check amount of lines
    for rows in text:
        max_rows += 1
    #give correct id to lines
    for lines in text:
        item = ""
        if max_rows>=id:
            lines = lines.split('|')
            lines[0] = id
            id +=1
        k = 0
        for elem in lines:
            if k == 8:
                item += str(elem)
            else:
                item += str(elem) + "|"
            k += 1
        x.writelines(item)
    x.close()
    refresh()

def backup():

    dest = "baza.txt " + str(datetime.date.today()) + " " + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute)
    shutil.copy("baza.txt", dest)

# MAIN WINDOW SIZE ETC.

root = Tk(className='Data')
root.config(bg='#F8F9FA')
nav = ttk.Frame(root, bootstyle="light")
nav.pack()
content = ttk.Frame(root)
content.pack(fill='y', expand=True)
fotter = ttk.Frame(root, bootstyle="light")
fotter.pack()
x = Label(fotter, bootstyle="light").grid(row=0, column=0)

addButton = tk.Button(nav, text='Add item', command=addWindow, font='Calibri 14')
addButton.grid(row=0, column=0, ipady=4, padx=30)

searchbar = Entry(nav, width=50, font='Calibri 14')
searchbar.bind("<KeyRelease>", dataGain)
searchbar.grid(row=0, column=1, ipady=5, padx=30)

searchtype = StringVar(content)
type = OptionMenu(nav, searchtype, "ID", "ID", "type", "name", "CECQ code", "QR code", "location", "placement","edition date", command=dataGain).grid(row=0, column=2, ipady=8, padx=30)


searchtype = StringVar(content)
type = OptionMenu(nav, searchtype, "ID", "ID", "type", "name", "CECQ code", "QR code", "location", "placement",
                  "edition date", command=dataGain)
type.grid(row=0, column=2, ipady=8, padx=30)

# MAIN LIST

columns = ('ID', 'type', 'name', 'CECQ code', 'QR code', 'location', 'placement', 'edition date', 'description')
listBox = Treeview(content, columns=columns, show='headings', height=40)
listBox.pack(fill='y', expand=True, side=LEFT)
scroll = ttk.Scrollbar(content, orient="vertical", command=listBox.yview)
scroll.pack(side=RIGHT, fill='y', expand=True)
listBox.configure(yscrollcommand=scroll.set)
listBox.bind('<Double-Button-1>', editRowWindow)
listBox.bind("<Delete>",delete_item)


for col in columns:
    listBox.heading(col, text=col,anchor=CENTER)
headings=('ID', 'type', 'name', 'CECQ code', 'QR code', 'location', 'placement', 'edition date', 'description')


style = ttk.Style()
style.configure('Treeview', rowheight=30)
style.configure("Treeview.Heading", background="#d2d2d2", foreground="black", font='Calibri 14')
style.configure('My.TFrame',background='red')

for col in columns:
    listBox.heading(col, text=col)
    listBox.column(col,anchor=CENTER)

changeColumnWidth(40, 'ID')
changeColumnWidth(150, 'type', 'edition date', 'placement')

id_update()
backup()
refresh()
root.mainloop()