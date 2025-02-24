def vogal(palavra):
    qtde = 0
    for i in palavra:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            qtde += 1
    return qtde

def reverso(palavra):
    return palavra[::-1]

def conta(texto):
    qtde = 1
    for i in texto:
        if i == ' ':
            qtde += 1
    return qtde