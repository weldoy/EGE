# ПЕРЕВОЛ В ДРУГУЮ СИСТЕМУ ИСЧИСЛЕНИЯ

n = 486473
string = ''

while n > 0:
    string += str(n % 3)
    n //= 3

print(string[::-1])
