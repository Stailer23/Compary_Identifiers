import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import umts_main
import main
filename1 = ''
filename2 = ''
select_folder = ''
def openfile1():
    '''
    Вызывает окно с выбором файла с зарагестрированными РЭС. Проверяет расширение.
    '''
    global filename1
    root.withdraw()
    filename1 = tkinter.filedialog.askopenfilename(filetypes=(("TXT", "*.txt"), ("All files", "*.*")))
    root.deiconify()
    e1.delete(0, END)
    e1.insert(0, filename1)

def zap_bs():
    if comboExample.get() == 'UMTS':
        umts_main.open_base(filename1)
        comboExample['state'] = 'disabled'
    elif comboExample.get() == 'LTE':
        main.open_base(filename1)
        comboExample['state'] = 'disabled'
    elif comboExample.get() == 'GSM':
        pass

def openfile2():
    '''
    Вызывает окно с выбором файла с зарагестрированными РЭС. Проверяет расширение.
    '''
    global filename2
    root.withdraw()
    filename2 = tkinter.filedialog.askopenfilename(filetypes=(("TXT", "*.txt"), ("All files", "*.*")))
    root.deiconify()
    e2.delete(0, END)
    e2.insert(0, filename2)

def selectFolderPath():
    '''
    Вызывает окно для выбора папки сохранения
    '''
    global select_folder
    root.withdraw()
    select_folder = tkinter.filedialog.askdirectory()
    root.deiconify()
    e4.delete(0, END)
    e4.insert(0, select_folder)

def run():
    delta = e5.get()
    delta_coord1 = e6.get()
    delta_coord2 =e7.get()
    if comboExample.get() == 'LTE':
        main.open_mes(filename2,delta,delta_coord1, delta_coord2)
        main.save(select_folder)
        l1 = Label(root, text = "Готово")
        l1.place(x=10, y = 280)
    elif comboExample.get() == 'UMTS':
        umts_main.open_mes(filename2,delta, delta_coord1, delta_coord2)
        umts_main.save(select_folder)
        l1 = Label(root, text = "Готово")
        l1.place(x=10, y = 280)
    elif comboExample.get() == 'GSM':  # Дописать когда будет GSM
        print('3')
    else: print ('4')


root = Tk()
root.title('Сид парсер здорового человека v1.5')
root.geometry('570x300+400+100')
root.resizable(False, False)
fl = LabelFrame(root,text = 'Выберите файл с базой (.txt)')
fl.place(x=10,y=105)
e1 = Entry(fl,width = 60)
e1.pack()

b1 = Button(root, text = 'Обзор..',width = 9, command = openfile1)
b1.place(x=380, y=110)
b2 = Button(root, text = 'Добавить в базу',width = 13, command = zap_bs)
b2.place(x=460, y = 110)

fl2 = LabelFrame(root,text = 'Выберите измерительный файл (.txt из ROMES)')
fl2.place(x=10,y=150)
e2 = Entry(fl2,width=60)
e2.pack()
b3 = Button(root, text = 'Обзор..',width = 9, command = openfile2)
b3.place(x=380, y=150)
b4 = Button(root, text='Старт', width=15, command=run)
b4.place(x=150, y=260)

fl3 = LabelFrame(root, text='Выбери папку для выгрузки')
fl3.place(x=10, y=200)
e4 = Entry(fl3, width=60)
e4.pack()
b5 = Button(root, text='Обзор..', width=9, command=selectFolderPath)
b5.place(x=380, y=200)

fl4 = LabelFrame(root,text='Настройки', width=100)
fl4.place(x=10, y=5)
l1 = Label(fl4, text='Стандарт ОПСОСа:')
l1.grid(row=0, column=0)

comboExample = ttk.Combobox(fl4, values=['GSM', 'UMTS', 'LTE'], width=5)
comboExample.current(2)
comboExample['state'] = 'readonly'
comboExample.grid(row=0, column=1, padx=5, pady=5)

l4 = Label(fl4, text='Дельта при поиске(км):')
l4.grid(row=0, column=2)
e5 = Entry(fl4, width=8)
e5.insert(0, '0.5')
e5.grid(row=0, column=3, padx=5, pady=5)

l5 = Label(fl4, text='Дельта широты(град.)')
l5.grid(row=1, column=0)
e6 = Entry(fl4, width=8)
e6.insert(0, '0.005')
e6.grid(row=1, column=1, pady=5)

l6 = Label(fl4, text='Дельта долготы(град.)')
l6.grid(row=1, column=2)
e7 = Entry(fl4, width=8)
e7.insert(0, '0.005')
e7.grid(row=1, column=3)


copirate = Label(root, text='by Nikolaev', fg='grey')
copirate.place(x=500, y = 280)

root.mainloop()