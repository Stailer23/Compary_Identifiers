def operator_base(line:list, mnc:int, dict:dict):
    if int(line[11]) == mnc:
        if line[14] not in dict.keys():
            dict[line[14]] = set()
            dict[line[14]].add(line[13])
        else:
            for key in dict.keys():
                if key == line[14]:
                    dict[key].add(line[13])
    else:
        return
    return dict

def serch(line, mnc, dict:dict, sheet,reply):
        if float(line[4]) >0 and float(line[4]) <0.5:
            if int(line[12]) == mnc:
                if line[0] in reply:
                    return

                if line[15] in dict.keys(): #если есть номер канал в ключах, то поискать ECI в ключе.
                    if line[14] in dict.get(line[15]): #Если в этом ключе найден ECI, то выйти
                        reply.append(line[0])
                        return
                    for key in dict.keys(): #Поискать по остальным ключам
                        if line[14] in dict.get(key): # Если нашлось
                            err = (f'Другой канал: {line[15]}, должен быть: {key}')
                            line.insert(0, err)
                            sheet.append(line)
                            reply.append(line[0])
                            return
                    if line[0] in reply:
                        return
                    err1 = (f'Нет такого ECI {line[14]}')
                    line.insert(0, err1)
                    sheet.append(line)
                    reply.append(line[0])
                    return
                else:
                    err2 = (f'Нет такого канала {line[15]}')
                    line.insert(0, err2)
                    sheet.append(line)
                    reply.append(line[0])
                    return
            else: return
        else: return

