# import linecache
# import time
# import ttkwidgets
# import shutil
# import ttkbootstrap
# import keyboard
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
import datetime
from ttkbootstrap.constants import *
import os


def changeColumnWidth(size, *args):
    for i in args:
        listBox.column(i, width=size)


def editRowWindow(event):
    selected = listBox.focus()
    currentID = int((listBox.item(selected, 'values')[0]))

    def editItem():
        edit_tab = str(
            currentID) + '|' + typeLabelValue.get() + '|' + nameLabelValue.get() + '|' + cecqLabelValue.get() + '|' + qrLabelValue.get() + '|' + locationLabelValue.get() + '|' + placementLabelValue.get() + '|' + str(
            datetime.date.today()) + '|' + descriptionLabelValue.get() + '\n'

        with open('baza.txt', 'r',encoding='utf-8') as file:
            data = file.readlines()
        data[currentID - 1] = edit_tab
        file.close()
        with open('baza.txt', 'w',encoding='utf-8') as file:
            file.writelines(data)
        file.close()
        refresh()

    def deleteItemButton():
        selected = listBox.focus()
        empty = ''

        with open('baza.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        data[currentID - 1] = empty
        file.close()
        with open('baza.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        file.close()
        id_update()
        refresh()
        editWindow.destroy()

    global if_closed
    editWindow = tkinter.Toplevel(root)
    editWindow.geometry("550x450")
    editFrame = ttk.Frame(editWindow, padding=50)
    editFrame.pack()
    if_closed = editWindow
    editColumn1 = ttk.Frame(editFrame)
    editColumn1.pack(side=LEFT)
    editColumn2 = ttk.Frame(editFrame)
    editColumn2.pack(side=LEFT)
    def bindOnClosing():
        listBox.bind('<Double-Button-1>', editRowWindow)
        editWindow.destroy()

    if editWindow.state() == "normal":
        print('open')
        listBox.unbind('<Double-Button-1>')

    editWindow.protocol("WM_DELETE_WINDOW", bindOnClosing)




    selected = listBox.focus()
    x = (listBox.item(selected, 'values'))

    typeLabel = Label(editColumn1, text='Type:', font='Calibri 14', anchor='w', width=10).pack()
    typeLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    typeLabelValue.insert(END, x[1])
    typeLabelValue.pack()

    nameLabel = ttk.Label(editColumn1, text='Name:', font='Calibri 14', anchor='w', width=10).pack()
    nameLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    nameLabelValue.insert(END, x[2])
    nameLabelValue.pack()

    cecqLabel = ttk.Label(editColumn1, text='Cecq:', font='Calibri 14', anchor='w', width=10).pack()
    cecqLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    cecqLabelValue.insert(END, x[3])
    cecqLabelValue.pack()

    qrLabel = ttk.Label(editColumn1, text='Qr code:', font='Calibri 14', anchor='w', width=10).pack()
    qrLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    qrLabelValue.insert(END, x[4])
    qrLabelValue.pack()

    locationLabel = ttk.Label(editColumn1, text='location:', font='Calibri 14', anchor='w', width=10).pack()
    locationLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    locationLabelValue.insert(END, x[5])
    locationLabelValue.pack()

    placementLabel = ttk.Label(editColumn1, text='placement:', font='Calibri 14', anchor='w', width=10).pack()
    placementLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    placementLabelValue.insert(END, x[6])
    placementLabelValue.pack()

    # editionDateLabel = ttk.Label(editColumn1, text='edition date', font='Calibri 14', anchor='w', width=10).pack()
    # editionDateLabelValue = ttk.Entry(editColumn2, font='Calibri 14', width=20)
    # placementLabelValue.insert(END, x[7])
    # editionDateLabelValue.pack()

    descriptionLabel = ttk.Label(editColumn1, text='description:', font='Calibri 14', anchor='w', width=10).pack()
    descriptionLabelValue = ttk.Entry(editColumn2, text=x[8], font='Calibri 14', width=20)
    descriptionLabelValue.insert(END, x[8])
    descriptionLabelValue.pack()

    removeItemButton = tk.Button(editWindow, text="Remove", font='Calibri 14', command=deleteItemButton).pack(side=LEFT,
                                                                                                              padx=20,
                                                                                                              pady=5,
                                                                                                              ipadx=10)
    EditButton = tk.Button(editWindow, text='Edit', font='Calibri 14', command=editItem).pack(side=LEFT, pady=5,
                                                                                              ipadx=10)


def refresh():
    with open('baza.txt',encoding='utf-8') as reader, open('baza.txt', 'r+',encoding='utf-8') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()
    x = open('baza.txt', 'r',encoding='utf-8')
    for row in listBox.get_children():
        listBox.delete(row)
    for line in x:
        table = []
        table = line.split("|")
        listBox.insert('', 'end', value=table)
    x.close()


def dataGain(item):
    x = open("baza.txt", "r",encoding='utf-8')
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
    xr = open("baza.txt", "r",encoding='utf-8')

    def dis_button():
        addButton["state"] = "normal"
        win.destroy()

    def addData():
        empty_line = ""
        xa = open("baza.txt", "a",encoding='utf-8')
        new_item.append(type.get())
        new_item.append(name.get())
        new_item.append(cecq.get())
        new_item.append(qr.get())
        new_item.append(location.get())
        new_item.append(placement.get())
        new_item.append(str(datetime.date.today()))
        new_item.append(description.get())
        i = 0
        for i in range(1, 7):
            empty_line += new_item[i]
        if empty_line:
            xa.write('\n')
            for item in new_item:
                xa.write(str(item) + "|")
                i += 1

        xa.close()
        xr.close()
        refresh()
        win.destroy()
        addWindow()

    global if_closed
    win = tkinter.Toplevel(root)
    win.grab_set()
    if_closed = win
    frame = Frame(win, padding=20)
    frame.grid(row=1, column=3)

    new_item = []
    if os.stat("baza.txt").st_size == 0:
        last_line = '0'
    else:
        last_line = ''
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

    try:
        if win.state() == "normal":
            addButton["state"] = "disable"
    except:
        pass
    win.protocol("WM_DELETE_WINDOW", dis_button)

def delete_item(event):
    selected = listBox.focus()
    currentID = int((listBox.item(selected, 'values')[0]))
    empty = ''

    with open('baza.txt', 'r',encoding='utf-8') as file:
        data = file.readlines()
    data[currentID - 1] = empty
    file.close()
    with open('baza.txt', 'w',encoding='utf-8') as file:
        file.writelines(data)
    file.close()
    id_update()
    refresh()


def id_update():
    i = 0
    with open('baza.txt', 'r',encoding='utf-8') as file:
        data = file.readlines()
        temp = []
        i = 1
        znak = '|'
    for line in data:
        if znak in line:
            x = line.index(znak)
        temp.append(str(i) + line[x:])
        i += 1
    file.close()
    with open('baza.txt', 'w',encoding='utf-8') as file:
        file.writelines(temp)
    file.close()



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
type = OptionMenu(nav, searchtype, "ID", "ID", "type", "name", "CECQ code", "QR code", "location", "placement",
                  "edition date", command=dataGain).grid(row=0, column=2, ipady=8, padx=30)

# MAIN LIST

columns = (
    'ID', 'type', 'name', 'CECQ code', 'QR code', 'location', 'placement', 'edition date', 'description')
listBox = Treeview(content, columns=columns, show='headings', height=40)
listBox.pack(fill='y', expand=True, side=LEFT)
scroll = ttk.Scrollbar(content, orient="vertical", command=listBox.yview)
scroll.pack(side=RIGHT, fill='y', expand=True)
listBox.configure(yscrollcommand=scroll.set)
listBox.bind('<Double-Button-1>', editRowWindow)
listBox.bind("<Delete>", delete_item)

for col in columns:
    listBox.heading(col, text=col, anchor=CENTER)
    listBox.column(col, anchor=CENTER)

changeColumnWidth(40, 'ID')
changeColumnWidth(150, 'type', 'edition date', 'placement')

style = ttk.Style()
style.configure('Treeview', rowheight=30)
style.configure("Treeview.Heading", background="#d2d2d2", foreground="black", font='Calibri 14')

def on_closing():
    try:
        if if_closed.state() == "normal":
            pass
    except:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
id_update()
refresh()
root.mainloop()
