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
#ip = input('Введите IP адрес: ')
ip = '172.16.228.69'
verif = []
for octet in ip.split('.'):
    verif.append(octet)
    if octet.isdigit() and int(octet) in range(0,255):
        print(octet)
    #if octet.isdigit() and octet in range(0,255):
        #verif.append(octet)
    #else:
        #break
if verif == ip:
    print('xyu')
print(verif)
print(ip)
    

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            

