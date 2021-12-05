# def operator_base(line:list, mnc:int, dict:dict, d_co:dict):
#     if int(line[11]) == mnc:
#         if line[14] not in dict.keys():
#             dict[line[14]] = set()
#             dict[line[14]].add(line[13])
#         else:
#             for key in dict.keys():
#                 if key == line[14]:
#                     dict[key].add(line[13])
#     else:
#         return
#     return dict
#
# def base_coord(line:list, mnc:int, dict_cooord:dict):
#     if int(line[11]) == mnc:
#         dict_cooord[line[13]] = set()
#         dict_cooord[line[13]].add(line[1])
#         dict_cooord[line[13]].add(line[2])
#     else:
#         return
#     return dict_cooord
#
# r = 'Adres;56,456464;43,34343;0;0;0;0;0;0;0;0;11;0;123123;5050;0;1'
# r=r.split(';')
# d = {}
# d_coord = {}
# b = base_coord(r,11, d_coord)
# print(d_coord)
# '''
# '''
# dict_test = {}
# # r = 'БС-NN0616:603069, Нижегородская обл., г. Нижний Новгород, Рельсовая ул.:619-рчс-19-0097:52 19 018183:действующее;43.7875;56.2056;0;0;0;40;0;0;0;0;10612;36165;02019;0;0;0;0;0;;250;20;;;0;8000;;;;;;;;;;;;;1;'
# # b = 'БС-NN0616:603069, Нижегородская обл., г. Нижний Новгород, Рельсовая ул.:619-рчс-19-0097:52 19 018183:действующее;43.7875;56.2056;0;0;0;40;0;0;0;0;10613;36162;02019;0;0;0;0;0;;250;20;;;0;8000;;;;;;;;;;;;;1;'
# # r = r.split(';')
# # b = b.split(';')
# with open('UMTS_20211108_090605.txt', 'r') as base:
#     for line in base:
#         line = line.split(';')
#         operator_base_umts(line,20,10612,dict_test)
# print(dict_test)
# d = {'abc':{123, 321}, 'bbb':{'sdsd':{'efef',12312}}}
# def writeBS(dict):
#     with open ('dbL.txt', 'w') as dbL:
#         for key,val in dict.items():
#             dbL.write(f'{key}:{val}\n')
# #
# writeBS(d)
# def readBS(file):
#     d={}
#     with open('dbL.txt', 'r') as readdbL:
#         for i in readdbL.readlines():
#             key,*val = i.strip().split(':')
#             d[key] = set(val)
#     return d
# print(d)
# print(readBS('dbL.txt'))
import datetime
a = datetime.datetime.now()
a = str(a)
print(a)