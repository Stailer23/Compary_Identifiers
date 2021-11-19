def operator_base(line:list, mnc:int, dict:dict, d_co:dict):
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

def base_coord(line:list, mnc:int, dict_cooord:dict):
    if int(line[11]) == mnc:
        dict_cooord[line[13]] = set()
        dict_cooord[line[13]].add(line[1])
        dict_cooord[line[13]].add(line[2])
    else:
        return
    return dict_cooord

r = 'Adres;56,456464;43,34343;0;0;0;0;0;0;0;0;11;0;123123;5050;0;1'
r=r.split(';')
d = {}
d_coord = {}
b = base_coord(r,11, d_coord)
print(d_coord)
