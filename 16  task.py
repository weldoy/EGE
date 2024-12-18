# def f(n):
#     if n > 0 and n % 2 == 0:
#         return f(n / 2)
#     elif n % 2 == 1:
#         return 1 + f(n - 1)
#     return 0
#
#
# count = 0
# for i in range(1, 1001):
#     if f(i) == 3:
#         count += 1
#
# print(count)

# -------------------------------------

# def f(n):
#     if n > 1 and n % 2 == 1:
#         return f(n-1) + 3*n**2
#     elif n > 1 and n % 2 == 0:
#         return n / 2 + f(n-1) + 2
#     else:
#         return 0
#
#
# print(f(49))
