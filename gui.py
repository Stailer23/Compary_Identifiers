import tkinter.filedialog
from tkinter import *
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
    main.open_base(filename1)

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
    main.open_mes(filename2)
    main.save(select_folder)
    l1 = Label(root, text = "Готово")
    l1.place(x=10, y = 180)


root = Tk()
root.title('Сид парсер здорового человека')
root.geometry('570x200+400+100')
root.resizable(False, False)
fl = LabelFrame(root,text = 'Выберите файл с базой (.txt)')
fl.place(x=10,y=5)
e1 = Entry(fl,width = 60)
e1.pack()

b1 = Button(root, text = 'Обзор..',width = 9, command = openfile1)
b1.place(x=380, y=10)
b2 = Button(root, text = 'Добавить в базу',width = 13, command = zap_bs)
b2.place(x=460, y = 10)

fl2 = LabelFrame(root,text = 'Выберите измерительный файл (.txt из ROMES)')
fl2.place(x=10,y=50)
e2 = Entry(fl2,width = 60)
e2.pack()
b3 = Button(root, text = 'Обзор..',width = 9, command = openfile2)
b3.place(x=380, y=50)
b4 = Button(root, text = 'Старт',width = 15, command = run)
b4.place(x=150, y = 160)

fl3 = LabelFrame(root,text = 'Выбери папку для выгрузки')
fl3.place(x=10,y=100)
e4 = Entry(fl3,width = 60)
e4.pack()
b5 = Button(root, text = 'Обзор..',width = 9, command = selectFolderPath)
b5.place(x=380, y=100)

copirate = Label(root, text = 'by Nikolaev', fg = 'grey')
copirate.place(x=500, y = 180)

root.mainloop()