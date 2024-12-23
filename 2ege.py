# from itertools import product, permutations

# def f(x, y, w, z):
#     return w and ((x <= y) == (y <= z))

# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6): # перебирает все возможные значения 0;1 в переменных 6 раз
#     t = (
#     (0, x1, x2, x3, 1),
#     (0, 0, x4, 0, 1),
#     (0, x5, x6, 0, 1)
#     )
#     if len(t) == len(set(t)): # set() убирает повторения строк
#         for p in permutations('xywz', r=4): # перебирает все возможные перестановки xywz, значение в ковычках совпадает с арг f(...)
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(*p)

# <-------------------------------------------------------->

# from itertools import product, permutations

# def u(x, y, z, w):
#     return (x <= (y <= z)) and (y <= (z == (not w)))

# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#     (0, 0, x1, 0, 0),
#     (0, 0, x2, x3, 0),
#     (x4, 0, x5, x6, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(u(**dict(zip(p, m))) == m[-1] for m in t):
#                 print(*p)

# <-------------------------------------------------------->

from itertools import product, permutations

def f(x, y, w, z):
    return ((x == z) <= ((not y) or w)) == (not ((w <= z) or (x <= y)))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1, 1, x2, 0, 1),
        (0, x3, 1, x4, 1),
        (0, x5, 0, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4): # значение в ковычках совпадает с арг f(...)
            if all(f(**dict(zip(p, m))) == m[-1] for m in t):
                print(*p)
