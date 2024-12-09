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
