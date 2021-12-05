def operator_base_umts(line:list, mnc:int, channel:int, dict:dict):
    if int(line[21]) == mnc and int(line[11]) == channel:  #21-mnc
        if line[13] not in dict.keys(): #LAC
            dict[line[13]] = set()
            dict[line[13]].add(line[12])
        else:
            for key in dict.keys():
                if key == line[13]:
                    dict[line[13]].add(line[12])
    else:
        return
    return dict

def base_coord_umts(line: list, dict_cooord: dict):
    if line[12] not in dict_cooord.keys():
        dict_cooord[line[12]] = set()
        dict_cooord[line[12]].add(line[1])
        dict_cooord[line[12]].add(line[2])
    else:
        return
    return dict_cooord

def serch(line, mnc, channel, dict: dict, dict_coord: dict, sheet, reply, delta, delta_coord1, delta_coord2):
    if float(line[4]) > 0 and float(line[4]) < float(delta):
        if int(line[12]) == mnc and int(line[15]) == channel:
            if line[0] in reply:
                return
            if len(line[13]) < 1:
                return
            laclen(line)
            if line[13] in dict.keys():  # если есть LAC в ключах, то поискать CI в ключе.
                if line[14] in dict.get(line[13]):  # Если в этом ключе найден CI, то выйти
                    reply.append(line[0])
                    ser_cor = serch_coord(line, dict_coord, line[14], delta_coord1, delta_coord2)
                    if ser_cor == True:
                        return
                    elif False in ser_cor:
                        print(ser_cor)
                        err3 = (f'Далековато. В базе: {ser_cor[1]}, {ser_cor[2]}')
                        line[1] = decdeg2dms(float(line[1]))  # Преобразование координат
                        line[2] = decdeg2dms(float(line[2]))  # Преобразование координат
                        line[1], line[2] = line[2], line[1]
                        line.insert(0, err3)
                        sheet.append(line)
                        reply.append(line[0])
                    return
                for key in dict.keys():  # Поискать по остальным ключам
                    if line[14] in dict.get(key):  # Если нашлось
                        err = (f'Другой LAC: {line[13]}, должен быть: {key}')
                        line[1] = decdeg2dms(float(line[1]))  # Преобразование координат
                        line[2] = decdeg2dms(float(line[2]))  # Преобразование координат
                        line[1], line[2] = line[2], line[1]
                        line.insert(0, err)
                        sheet.append(line)
                        reply.append(line[0])
                        return
                if line[0] in reply:
                    return
                err1 = (f'Нет такого CI {line[14]}')
                line[1] = decdeg2dms(float(line[1]))  # Преобразование координат
                line[2] = decdeg2dms(float(line[2]))  # Преобразование координат
                line[1], line[2] = line[2], line[1]
                line.insert(0, err1)
                sheet.append(line)
                reply.append(line[0])
                return
            else:
                err2 = (f'Нет такого LAC {line[13]}')
                line[1] = decdeg2dms(float(line[1]))  # Преобразование координат
                line[2] = decdeg2dms(float(line[2]))  # Преобразование координат
                line[1], line[2] = line[2], line[1]
                line.insert(0, err2)
                sheet.append(line)
                reply.append(line[0])
                return
        else:
            return
    else:
        return

def serch_coord(line, dict, key, delta_coord1, delta_coord2):
    a = float(line[2])
    b = float(line[1])
    c = []
    for i in (dict[key]):
        c.append(i)
    d,e = float(c[0]),float(c[1])
    if d<e:
        d,e = e,d
    if (abs(a - float(d)) > float(delta_coord1)) or (abs(b - float(e)) > float(delta_coord2)):
        # print(a,b,d,e,(abs(a - float(d))),(abs(b - float(e))))
        preobD = decdeg2dms(d)
        preobE = decdeg2dms(e)
        return [False, preobD, preobE]
    else:
        return True

def decdeg2dms(dd): #Преобразование координат
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return f'{int(degrees):02} {int(minutes):02} {int(seconds):02}'

def writeBS(dict, name):
    with open (name, 'w') as dbL:
        for key,val in dict.items():
            dbL.write(f'{key}:{val}\n')

def readBS(file):
    dict={}
    with open(file, 'r') as readdb:
        for i in readdb.readlines():
            key,val = i.strip().split(':')
            val = val.replace('{', '').replace('}', '').replace("'", '').replace(' ', '')
            val = val.split(',')
            val = set(val)
            dict[key] = val
    return dict

def laclen(line):
    if len(line[13]) == 5:
        return
    else:
        line[13] = f'0{line[13]}'
        laclen(line)
    return line