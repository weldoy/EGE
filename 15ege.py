def f(x, y , A):
    return (2 * x - 4 * y < A) or (y >= x) or (x > 67)

print(list(A for A in range(200) if all(f(x, y, A) == 1 for x in range(1, 400) for y in range(1, 400))))

# Шаблон, но можно разобраться/расписать 
