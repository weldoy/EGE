# from itertools import product, permutations
#
#
# def f(x, y, z, w):
#     return not (y <= x) or (z <= w) or not z
#
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
#     t = (
#         (x1, 0, x2, x3, 0),
#         (0, 1, x4, x5, 0),
#         (1, x6, x7, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(*p)


# from itertools import product, permutations
#
#
# def f(x, y, z, w):
#     return (w or not x) and (w == (not y)) and (w <= z)
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (1, x1, 1, 1, 1),
#         (x2, x3, 1, x4, 1),
#         (1, x5, 1, x6, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(*p)


# alphabet = 'ABCDX'
# count = 0
#
# for x1 in alphabet:
#     for x2 in alphabet:
#         for x3 in alphabet:
#             for x4 in alphabet:
#                 word = (x1+x2+x3+x4)
#                 if word.count('X') == 1:
#                     count += 1
#
# print(count)


# alphabet = 'УОА'
# count = 0
# arr = []
#
# for x1 in alphabet:
#     for x2 in alphabet:
#         for x3 in alphabet:
#             for x4 in alphabet:
#                 for x5 in alphabet:
#                     for x6 in alphabet:
#                         word = (x1+x2+x3+x4+x5+x6)
#                         count += 1
#                         arr.append(word)
#
# print(arr.index('ОУУУОО') + 1)


# x = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
# string = 0
#
# while x > 0:
#     if x % 3 == 2:
#         string += 1
#     x //= 3
#
# print(string)


arr = []

for x in '012345678':
    f = int(f'88{x}4{x}', 9) + int(f'7{x}344', 9)
    if f % 67 == 0:
        print(f // 67, x)
