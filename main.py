# 5 ЗАДАНИЕ

# f_numbers = []
# for n in range(4, 2000):
#     f = bin(n)[2:]
#     if n % 3 == 0:
#         f += f[-3:]
#     else:
#         f += bin(n % 3 * 3)[2:]
#     if int(f, 2) <= 170:
#         f_numbers.append(int(f, 2))
#         print(f'{int(f, 2)}, {f=}, {n=}')
# print(sorted(f_numbers))

# -------------------------------------------------

# 15 ЗАДАНИЕ

# for A in range(1, 1000):
#     like = True  # Флаг - нравится нам параметр А или нет
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             f = (x < A) or (y < A) or (x + 2*y > 50)
#             if not f:
#                 like = False
#                 break
#
#         if not like:
#             break
#     if like:
#         print(f'{A=}')

# -------------------------------------------------

# 16 ЗАДАНИЕ

# import sys
#
# sys.setrecursionlimit(3000)  # Удалить лимит рекурсий
#
#
# def f(n):
#     return n if n < 11 else n + f(n - 1)
#     # if n < 11:
#     #     return n
#     # else:
#     #     return n + f(n - 1)
#
#
# print(f(2024) - f(2021))

# -------------------------------------------------

# 14 ЗАДАНИЕ

# numbers = []
# for y in '01234567':
#     for x in range(1, 8): # Не от нуля, тк x в начале стоит
#         number = int(f'{x}01{y}4', 9) + int(f'{x}{y}544', 8)
#         if number % 89 == 0:
#             numbers.append(number)
# print(min(numbers)//89)

# -------------------------------------------------

# 6 ЗАДАНИЕ

# from turtle import *
#
# size = 10
# tracer(100)
#
# lt(90)
#
# for i in range(2):
#     fd(23 * size)
#     rt(90)
#     fd(10 * size)
#     rt(90)
#
# fd(3 * size)
# lt(90)
# fd(12 * size)
# rt(90)
#
# for i in range(2):
#     fd(9 * size)
#     rt(90)
#     fd(32 * size)
#     rt(90)
#
# up()
#
# for x in range(-20 * size, 30 * size, size):
#     for y in range(-10 * size, 30 * size, size):
#         goto(x, y)
#         dot(2)
#
# exitonclick()
