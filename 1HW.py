#! /usr/bin/python3
#1 
#     a = int(input('Введите число от 1 до 7: '))
#     if a > 7 or a < 1:
#         print('нет такого дня недели')
#     else:
#         if a >= 1 and a < 6:
#             print('нет')
#         else:
#             print('да')

# #2
# x = [0,1]
# y = [0,1]
# z = [0,1]
# fl = not(x or y or z)
# fr = not x and not y and not z
# if fl == fr:
#     print(True)
# else:
#     print(False)

# #3
# x = float(input('Введите координаты Х: '))
# y = float(input('Введите координаты Y: '))
# if x == 0 and y == 0:
#     print('точка в центре координатных осей')
# else:
#     if x != 0 and y == 0:
#         print('точка находится на оси Х')
#     else:
#         if x == 0 and y != 0:
#             print('точка находится на оси Y')
#         else:
#             if x > 0 and y > 0:
#                 print('I четверть')
#             else:
#                 if x < 0 and y > 0:
#                     print('II четверть')
#                 else:
#                     if x < 0 and y < 0:
#                         print('III четверть')
#                     else:
#                         if x > 0 and y < 0:
#                             print('IV четверть')
#                         else: 
#                             print('err')

# #4
# a = int(input('Введите номер четверти: '))
# if a == 1:
#     print('x(0,∞)\ny(0,∞)')
# else:
#     if a == 2:
#         print('x(-∞,0)\ny(0,∞)')
#     else:
#         if a == 3:
#             print('x(-∞,0)\ny(-∞,0)')
#         else:
#             if a == 4:
#                 print('x(0,∞)\ny(-∞,0)')
#             else:
#                 print('нет такой четверти')

#5
print('Введите координаты точки A')
ax = float(input())
ay = float(input())
print ('Введите координаты точки B')
bx = float(input())
by = float(input())
from math import sqrt
s = sqrt((ax - bx)**2 + (ay - by)**2)
print('Расстояние между точками А и В = ',s)
