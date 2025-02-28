def criar_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)

    print("Matriz criada:")
    for linha in matriz:
        print(linha)

criar_matriz()