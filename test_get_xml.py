import os
import xml.etree.ElementTree as ET

tree = ET.parse(r"D:\data\module\params\database.xml")

root = tree.getroot()

section = "postgresql"
pattern = section + "/"
objs = tree.findall(pattern)

#print(item.get('database'))
result = {}
for item in objs:
    a = item.tag
    b = item.text
    result[str(a)] = str(b)
    #print(item.tag)
    #print(item.text)

print(result)
"""for item in root.findall("./mariadb"):
    print(item.tag)
    print(item.attrib)
    print(item.text)
result_list = []"""
#for item in tree.findall("mariadb"):
#for item in tree.iterfind("mariadb"):
#    print(item.attrib)
"""print(item.get('database'))
    db = {}
    db['database'] = item.get('database')
    db['host'] = item.get('host')
    db['port'] = item.get('port')
    db['user_own'] = item.get('user_own')
    db['user_app'] = item.get('user_app')
    result_list.append(db)"""



#print(result_list)