import funcs, openpyxl
t2_base = {}
mts_base = {}
megafon_base = {}
beeline_base = {}
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
            funcs.operator_base(line_base, 99, mts_base)
            funcs.operator_base(line_base, 20, t2_base)
            funcs.operator_base(line_base, 0, t2_base)
            print('раз база')
def open_mes(filename):
    with open(filename) as mes:
        for line_mes in mes:
            line_mes = line_mes.split(';')
            funcs.serch(line_mes, 11, megafon_base, sheet,reply)
            funcs.serch(line_mes, 2, megafon_base,sheet,reply)
            funcs.serch(line_mes, 1, mts_base,sheet,reply)
            funcs.serch(line_mes, 99, mts_base,sheet,reply)
            funcs.serch(line_mes, 20, t2_base,sheet,reply)
            funcs.serch(line_mes, 0, t2_base,sheet,reply)

def save(direct):
    wb.save(f'{direct}/Нарушения.xlsx')




