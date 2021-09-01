# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP адрес: ')

pravilno = False
while not pravilno:
    verif = []
    for octet in ip.split('.'):
        if octet.isdigit() and int(octet) in range(0,256):
            verif.append(octet)
        else:
            break
    if not ip.count('.') == 3 or not len(ip.split('.')) == 4 or not verif == ip.split('.'):
        print('Неправильный IP-адрес')
        ip = input('Введите IP адрес ещо раз: ')
    else:
        pravilno = True    
    
if int(ip.split('.')[0]) in range(1,223):
   print('unicast')
elif int(ip.split('.')[0]) in range(224,239):
   print('multicast')
elif ip == '255.255.255.255': 
   print('local broadcast')
elif ip == '0.0.0.0':
   print('unassigned')
else:
   print('unused')
