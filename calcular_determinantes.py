#A
def digitar_matrizes():
    matrizes = []
    while True:
        adicionar_matriz = str(input('Criar matriz? (s/n):\n'))
        if adicionar_matriz.upper() == 'S':
            linhas = int(input('Digite a quantidade de linhas:\n'))
            colunas = int(input('Digite a quantidade de colunas:\n'))

            matriz = criar_matriz(linhas = linhas, colunas = colunas)
            matrizes.append(matriz)
        else:   
            break

    return matrizes

def criar_matriz(linhas = 0, colunas = 0):
    matriz = []
    for linha in range(linhas):
        matriz.append([])
        for coluna in range(colunas):
            valor = int(input(f'Digite o valor a{linha + 1}{coluna + 1}: '))
            matriz[linha].append(valor)
        
    return matriz

#B
def determinante_existe(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False

#C
def calcular_cofator(determinante, linha = 1, coluna = 1):
    cofator = ((-1)**(linha + coluna)) * determinante
    return cofator

#D
def calcular_determinantes(matriz):
    ordem = len(matriz)

    if ordem == 1:
        determinante = matriz[0][0]

    elif ordem == 2:
        determinante = calcular_ordem_2(matriz)
    
    elif ordem == 3:
        determinante = calcular_sarrus(matriz)

    elif ordem > 3:
        determinante = calcular_laplace(matriz)

    return determinante

def calcular_ordem_2(matriz):
    ordem = 2
    diagonal_principal = 1
    diagonal_secundaria = 1
    for linha in range(ordem):
        for coluna in range(ordem):
            if linha == coluna:
                diagonal_principal *= matriz[linha][coluna]
            else:
                diagonal_secundaria *= matriz[linha][coluna]

    determinante = diagonal_principal - diagonal_secundaria
    return determinante

def calcular_sarrus(matriz):
    ordem = 3
    diagonais_principais = []
    diagonais_secundarias = []
    for y in range(ordem):
        diagonais_principais.append(1)
        diagonais_secundarias.append(1)

    for linha in range(ordem):    
        for coluna in range(ordem):           
            #PRINCIPAIS
            if linha == coluna:
                diagonais_principais[0] *= matriz[linha][coluna]
            elif (linha + 1) == coluna or (linha - 2) == coluna:
                diagonais_principais[1] *= matriz[linha][coluna]
            elif (linha + 2) == coluna or (linha - coluna) == 1:
                diagonais_principais[2] *= matriz[linha][coluna]

            #SECUNDARIAS
            if (linha + coluna) == 2:
                diagonais_secundarias[0] *= matriz[linha][coluna]
            elif (linha + coluna) == 0 or (linha + coluna) == 3:
                diagonais_secundarias[1] *= matriz[linha][coluna]
            elif (linha + coluna) == 4 or (linha + coluna) == 1:
                diagonais_secundarias[2] *= matriz[linha][coluna]

    diagonais_principais = sum(diagonais_principais)
    diagonais_secundarias = sum(diagonais_secundarias)

    determinante = diagonais_principais - diagonais_secundarias

    return determinante

def calcular_laplace(matriz):
    ordem = len(matriz)

    if ordem > 4:
        x = 0
        for elemento in matriz[0]:
            sub_matriz = criar_sub_matriz(matriz, linha_do_elemento = 0, coluna_do_elemento = x )
            x += 1
            calcular_laplace(sub_matriz)

    n = 0
    elementos_multiplicados_pelos_cofatores = []
    for elemento in matriz[0]:
        sub_matriz = criar_sub_matriz(matriz, linha_do_elemento = 0, coluna_do_elemento = n)
        n += 1
        determinante_sub_matriz = calcular_determinantes(sub_matriz)
        cofator_elemento = calcular_cofator(determinante_sub_matriz, linha = 1, coluna = n)

        elementos_multiplicados_pelos_cofatores.append(elemento * cofator_elemento)

    return sum(elementos_multiplicados_pelos_cofatores)

def criar_sub_matriz(matriz, linha_do_elemento = 0, coluna_do_elemento = 0):
    sub_matriz = []
    for x in range(len(matriz) - 1):
        sub_matriz.append([])

    i = 0
    linha_atual = 0
    for linha in matriz:
        if linha_atual != linha_do_elemento:
            coluna_atual = 0     
            for coluna in linha:      
                if coluna_atual != coluna_do_elemento:
                    sub_matriz[i].append(coluna)
                coluna_atual += 1
            i += 1
        linha_atual += 1

    return sub_matriz

#E
def exibir_matrizes_e_determinantes(matrizes):
    x = 1
    for matriz in matrizes:
        print(f'\nMatriz {x}')
        x += 1
        for linha in matriz:
            print(linha)

        if determinante_existe(matriz):
            determinante = calcular_determinantes(matriz)
            print(f'Determinante: {determinante}')
        else:
            print('Não é possível calcular o determinante desta matriz.')

matrizes = digitar_matrizes()
exibir_matrizes_e_determinantes(matrizes)
