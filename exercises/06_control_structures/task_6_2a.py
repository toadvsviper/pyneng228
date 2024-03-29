# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP адрес: ')
verif = []
for octet in ip.split('.'):
    if octet.isdigit() and int(octet) in range(0,256):
        verif.append(octet)
    else:
        break
if not ip.count('.') == 3 or not len(ip.split('.')) == 4 or not verif == ip.split('.'):
    print('Неправильный IP-адрес')
elif int(ip.split('.')[0]) in range(1,223):
   print('unicast')
elif int(ip.split('.')[0]) in range(224,239):
   print('multicast')
elif ip == '255.255.255.255': 
   print('local broadcast')
elif ip == '0.0.0.0':
   print('unassigned')
else:
   print('unused') 
    

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            

