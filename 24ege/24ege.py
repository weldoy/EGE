with open('24ege/inf_22_10_20_24.txt') as shit:
    result = 0
    symbols = []
    for elem in shit:
        for symbol in elem: 
            symbols += symbol
        if symbols.count('E') > symbols.count('A'):
            result += 1
        else:
            result = result
    
print(result)

# --------------------

f = open('24ege/inf_22_10_20_24.txt')
a = 0
for string in f:
    if(string.count('A') < string.count('E')):
        a += 1
print(a)
