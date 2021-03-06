# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
a = ospf_route.split()
a[1] = a[1].strip('[]')
a[3] = a[3].strip(',')
a[4] = a[4].strip(',')
ospf = {'Prefix':a[0],'AD/Metric':a[1],'Next-Hop':a[3],'Last update':a[4],'Outbound Interface':a[5]}
print(f'''
Prefix                {a[0]}
AD/Metric             {a[1]}
Next-Hop              {a[3]}
Last update           {a[4]}
Outbound Interface    {a[5]}
''')
