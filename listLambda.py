a = [i**2 for i in range(1,11)]
print(a)

a = []
for i in range(1,11):
    a.append(i**2)
print(a)

b =  [ i for i in range(1,21) if i % 2 == 0]
print(b)

palavras = [ "abacate", "banana", "caju", "dua", "elefante" ]

c = [ len(i) for i in palavras ]

