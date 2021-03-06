import funcs
import openpyxl
import datetime

t2_base = {}
mts_base = {}
megafon_base = {}
beeline_base = {}
coord = {}
reply = []
wb = openpyxl.Workbook()
wb.create_sheet(title='Нарушения', index=0)
sheet = wb.active
title = ['Вид нарушения', 'Название','Долгота','Широта','Погр','Погр.а1','Погр.а2',
         'Погр.азимут','Азимут','Мощь','Макс. уровень','TowerId','MCC',
         'MNC','TAC','ECI','Канал','PCI']
sheet.append(title)
def open_base(filename):
    with open(filename, 'r') as base:
         for line_base in base:

            line_base = line_base.split(';')
            funcs.operator_base(line_base, 1, mts_base)
            funcs.operator_base(line_base, 2, megafon_base)
            funcs.operator_base(line_base, 11, megafon_base)
            funcs.operator_base(line_base, 99, mts_base) #!!!!!!!!!!
            funcs.operator_base(line_base, 20, t2_base)
            funcs.operator_base(line_base, 0, t2_base)
            funcs.base_coord(line_base, coord)
    funcs.writeBS(t2_base,'dbt2L.txt')
    funcs.writeBS(mts_base,'dbmtsL.txt')
    funcs.writeBS(megafon_base,'dbmfL.txt')
    funcs.writeBS(coord, 'dbcoordL.txt')
    funcs.readBS('dbt2L.txt')

def open_mes(filename, delta,delta_coord1, delta_coord2):
    delta1 = delta.replace(',','.')
    megafon_base = funcs.readBS('dbmfL.txt')
    mts_base = funcs.readBS('dbmtsL.txt')
    t2_base = funcs.readBS('dbt2L.txt')
    coord = funcs.readBS('dbcoordL.txt')
    with open(filename) as mes:
        for line_mes in mes:
            line_mes = line_mes.split(';')
            funcs.serch(line_mes, 11, megafon_base, coord, sheet,reply, delta1,delta_coord1, delta_coord2)
            funcs.serch(line_mes, 2, megafon_base, coord, sheet,reply,delta1,delta_coord1, delta_coord2)
            funcs.serch(line_mes, 1, mts_base,coord, sheet,reply,delta1,delta_coord1, delta_coord2)
            funcs.serch(line_mes, 99, mts_base, coord, sheet,reply,delta1,delta_coord1, delta_coord2)
            funcs.serch(line_mes, 20, t2_base, coord, sheet,reply,delta1,delta_coord1, delta_coord2)
            funcs.serch(line_mes, 0, t2_base, coord, sheet,reply,delta1,delta_coord1, delta_coord2)

def save(direct):
    time = str(datetime.datetime.now()).replace(':', '-')
    wb.save(f'{direct}/Нарушения LTE {time}.xlsx')




