import funcs_umts, openpyxl, datetime
t2_base_umts1 = {}
t2_base_umts2 = {}
t2_base_umts3 = {}
mts_base_umts1 = {}
mts_base_umts2 = {}
mts_base_umts3 = {}
megafon_base_umts1 = {}
megafon_base_umts2 = {}
megafon_base_umts3 = {}
beeline_base_umts1 = {}
beeline_base_umts2 = {}
beeline_base_umts3 = {}
other = {}
coord_umts = {}
reply_umts = []
wb = openpyxl.Workbook()
wb.create_sheet(title='Нарушения_UMTS', index=0)
sheet = wb.active
title = ['Вид нарушения', 'Название','Долгота','Широта','Погр','Погр.а1','Погр.а2',
         'Погр.азимут','Азимут','Мощь','Макс. уровень','TowerId','MCC',
         'MNC','LAC','CI','Канал','SC']
sheet.append(title)

def open_base(filename):

    with open(filename, 'r') as base:
         for line_base in base:
            line_base = line_base.split(';')
            funcs_umts.operator_base_umts(line_base, 1,10762, mts_base_umts1)
            funcs_umts.operator_base_umts(line_base, 1,10737, mts_base_umts2)
            funcs_umts.operator_base_umts(line_base, 1,10713, mts_base_umts3)
            funcs_umts.operator_base_umts(line_base, 2,10687, megafon_base_umts1)
            funcs_umts.operator_base_umts(line_base, 2,10662, megafon_base_umts2)
            funcs_umts.operator_base_umts(line_base, 2,10638, megafon_base_umts3)
            funcs_umts.operator_base_umts(line_base, 99,10836, beeline_base_umts1)
            funcs_umts.operator_base_umts(line_base, 99,10813, beeline_base_umts2)
            funcs_umts.operator_base_umts(line_base, 99,10788, beeline_base_umts3)
            funcs_umts.operator_base_umts(line_base, 20,10612, t2_base_umts1)
            funcs_umts.operator_base_umts(line_base, 20,10587, t2_base_umts2)
            funcs_umts.operator_base_umts(line_base, 20,10563, t2_base_umts3)
            # funcs_umts.operator_base_umts(line_base, 0, t2_base)
            funcs_umts.base_coord_umts(line_base, coord_umts)
    funcs_umts.writeBS(mts_base_umts1, 'dbmtsU1.txt')
    funcs_umts.writeBS(mts_base_umts2, 'dbmtsU2.txt')
    funcs_umts.writeBS(mts_base_umts3, 'dbmtsU3.txt')
    funcs_umts.writeBS(megafon_base_umts1, 'dbmfU1.txt')
    funcs_umts.writeBS(megafon_base_umts2, 'dbmfU2.txt')
    funcs_umts.writeBS(megafon_base_umts3, 'dbmfU3.txt')
    funcs_umts.writeBS(beeline_base_umts1, 'dbvkU1.txt')
    funcs_umts.writeBS(beeline_base_umts2, 'dbvkU2.txt')
    funcs_umts.writeBS(beeline_base_umts3, 'dbvkU3.txt')
    funcs_umts.writeBS(t2_base_umts1, 'dbt2U1.txt')
    funcs_umts.writeBS(t2_base_umts1, 'dbt2U2.txt')
    funcs_umts.writeBS(t2_base_umts1, 'dbt2U3.txt')
    funcs_umts.writeBS(coord_umts, 'dbcoordU.txt')

def open_mes(filename, delta):
    delta1 = delta.replace(',','.')
    mts_base_umts1 = funcs_umts.readBS('dbmtsU1.txt')
    mts_base_umts2 = funcs_umts.readBS('dbmtsU2.txt')
    mts_base_umts3 = funcs_umts.readBS('dbmtsU3.txt')
    megafon_base_umts1 = funcs_umts.readBS('dbmfU1.txt')
    megafon_base_umts2 = funcs_umts.readBS('dbmfU2.txt')
    megafon_base_umts3 = funcs_umts.readBS('dbmfU3.txt')
    beeline_base_umts1 = funcs_umts.readBS('dbvkU1.txt')
    beeline_base_umts2 = funcs_umts.readBS('dbvkU2.txt')
    beeline_base_umts3 = funcs_umts.readBS('dbvkU3.txt')
    t2_base_umts1 = funcs_umts.readBS('dbt2U1.txt')
    t2_base_umts2 = funcs_umts.readBS('dbt2U2.txt')
    t2_base_umts3 = funcs_umts.readBS('dbt2U3.txt')
    coord_umts = funcs_umts.readBS('dbcoordU.txt')
    with open(filename) as mes:
        for line_mes in mes:
            line_mes = line_mes.split(';')
            funcs_umts.serch(line_mes, 2,10687, megafon_base_umts1, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 2, 10662, megafon_base_umts2, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 2,10638, megafon_base_umts3, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 1,10762, mts_base_umts1,coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 1,10737, mts_base_umts2,coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 1,10713, mts_base_umts3,coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 99,10836, beeline_base_umts1, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 99,10813, beeline_base_umts2, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 99,10788, beeline_base_umts3, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 20,10612, t2_base_umts1, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 20,10587, t2_base_umts2, coord_umts, sheet,reply_umts, delta1)
            funcs_umts.serch(line_mes, 20,10563, t2_base_umts3, coord_umts, sheet,reply_umts, delta1)


def save(direct):
    wb.save(f'{direct}/Нарушения UMTS.xlsx')

