# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip_mask = input('Введите IP-адрес и маску подсети: ')

ip = ip_mask[:ip_mask.index('/')].split('.')
o1,o2,o3,o4 = ip
o1,o2,o3,o4 = int(o1),int(o2),int(o3),int(o4)
ip_bin = f"{o1:08b}"+f"{o2:08b}"+f"{o3:08b}"+f"{o4:08b}"
mask = ip_mask[ip_mask.index('/')+1:]
binmask = '1'*int(mask)+'0'*(32-int(mask))

net_bin = ip_bin[0:int(mask)]+'0'*(32-int(mask))
net = [int(net_bin[0:8],2),int(net_bin[8:16],2),int(net_bin[16:24],2),int(net_bin[24:32],2)]
#print(net_bin)
#print(net)
print(f'''

Network:
{net[0]:<8} {net[1]:<8} {net[2]:<8} {net[3]:<8}
{net_bin[0:8]} {net_bin[8:16]} {net_bin[16:24]} {net_bin[24:32]:}

Mask:
/{mask}
{int(binmask[0:8],2):<8} {int(binmask[8:16],2):<8} {int(binmask[16:24],2):<8} {int(binmask[24:32],2):<8}
{binmask[0:8]:<8} {binmask[8:16]:<8} {binmask[16:24]:<8} {binmask[24:32]:<8}

''')
