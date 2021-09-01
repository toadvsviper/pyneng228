# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
filerd, filewr = argv[1::]    
ignore = ["duplex", "alias", "configuration"]
a = []
with open(filerd,'r') as f, open(filewr,'w') as n:
    for line in f:
        if not line.startswith('!'):
            if not set(line.split()) & set(ignore):
                a.append(line.rstrip()+'\n')
    n.writelines(a)
