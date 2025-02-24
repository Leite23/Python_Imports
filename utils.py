def vogais(palavra):

    qtde = 0
    for letra in palavra:
        if letra in "aeiou":
            qtde += 1
    return qtde

def palavra_invertida(palavra):

    invertida = f"{palavra[::-1]}"
    return (invertida)


def conta(texto):

    qtde = 0
    for letra in texto:
        if letra in "aeiou":
            qtde += 1
    return qtde