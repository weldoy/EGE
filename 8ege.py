count = 0
words = []
alphabet = 'АВНРЬЯ'
for n1 in alphabet:
    for n2 in alphabet:
        for n3 in alphabet:
            for n4 in alphabet:
                for n5 in alphabet:
                    word = list(n1+n2+n3+n4+n5)
                    count += 1
                    if word[0] != 'А' and word.count('Н') <= 1 and 'АА' not in ''.join(word):
                        words.append(f'{''.join(word)} : {count}')
print(min(words))
