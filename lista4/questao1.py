sequencia = input()

def bubbleSort(lista):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    numeroComp = 0
    numeroTroc = 0
    i = len(lista) - 1
    while i > 0:
        for j in range(i):
            numeroComp += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                numeroTroc += 1
        i -= 1
    return numeroComp, numeroTroc

def selectionSort(lista):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    numeroComp = 0
    numeroTroc = 0

    for i in range(len(lista) - 1):
        menor = i
        for j in range(i + 1, len(lista)):
            numeroComp += 1
            if lista[j] < lista[menor]:
                menor = j
        
        if menor != i:    
            numeroTroc += 1
            lista[menor], lista[i] = lista[i], lista[menor]
    
    return numeroComp, numeroTroc

def insertionSort(lista):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    
    numeroComp = 0
    numeroTroc = 0

    for i in range(1, len(lista)):
        valor = lista[i]
        # salvando o valor inicial
        j = i - 1
        
        while j >= 0 and lista[j] > valor:
        # checagem se o valor anterior é maior, caso seja ocorrerá a troca
            numeroTroc += 1
            numeroComp += 1
            lista[j + 1] = lista[j]
            j -= 1

        if j >= 0:
            numeroComp += 1

        lista[j + 1] = valor
    
    return numeroComp, numeroTroc

def shellSort(lista):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    metade = len(lista)//2
    numeroComp = 0
    numeroTroca = 0

    while metade > 0:
        for i in range(metade, len(lista)):
            valor = lista[i]
            j = i

            while j>= metade and lista[j - metade] > valor:
                numeroComp += 1
                numeroTroca += 1
                lista[j] = lista[j - metade]
                j -= metade
            
            if j >= metade:
                numeroComp += 1
            lista[j] = valor
        
        metade = metade//2
    
    return numeroComp, numeroTroca

numeroCompQuick = 0
numeroTrocaQuick = 0

# Colocando valores prévios para fim e inicio para facilitar na chamada
def quickSort(A, inicio=0, fim=None):
    # convertendo os valores para números inteiros
    for i in range(len(A)):
        A[i] = int(A[i])

    if fim == None:
        fim = len(A) - 1
    if inicio >= 0 and fim >= 0 and inicio < fim:
        p = partition(A, inicio, fim)
        quickSort(A, inicio, p)
        quickSort(A, p + 1, fim)

def partition(A, inicio, fim):
    pivot = A[(fim + inicio) // 2]
    i = inicio
    j = fim
    global numeroCompQuick
    global numeroTrocaQuick
    while True:
        if i >= j:
            return j
        while A[i] < pivot:
            numeroCompQuick += 1
            i += 1
        while A[j] > pivot:
            numeroCompQuick += 1
            j -= 1

        numeroTrocaQuick += 1 
        A[i], A[j] = A[j], A[i]

    return i

def bubbleSortLimitado(lista, numeroDeAcoes):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    
    i = len(lista) - 1
    while i > 0 and numeroDeAcoes > 0:
        for j in range(i):
            numeroDeAcoes -= 1
            if lista[j] > lista[j + 1] and numeroDeAcoes > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                numeroDeAcoes -= 1
        i -= 1
    return lista

def selectionSortLimitado(lista, numeroDeAcoes):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    
    while numeroDeAcoes > 0:    
        for i in range(len(lista) - 1):
            menor = i
            for j in range(i + 1, len(lista)):
                numeroDeAcoes -= 1
                if lista[j] < lista[menor]:
                    menor = j
            
            if menor != i and numeroDeAcoes > 0:    
                numeroDeAcoes -= 1
                lista[menor], lista[i] = lista[i], lista[menor]
    
    return lista

def insertionSortLimitado(lista, numeroDeAcoes):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    while numeroDeAcoes > 0:
        for i in range(1, len(lista)):
            valor = lista[i]
            # salvando o valor inicial
            j = i - 1
            
            while j >= 0 and lista[j] > valor and numeroDeAcoes > 0:
            # checagem se o valor anterior é maior, caso seja ocorrerá a troca
                numeroDeAcoes -= 1
                if numeroDeAcoes > 0:
                    numeroDeAcoes -= 1
                    lista[j + 1] = lista[j]
                    j -= 1
            
            if j>=0 and numeroDeAcoes > 0:
                numeroDeAcoes -= 1
                if numeroDeAcoes == 0:
                  lista[j+1] = valor
            
            if numeroDeAcoes > 0:
              lista[j + 1] = valor
    
    return lista

def shellSortLimitado(lista, numeroDeAcoes):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    metade = len(lista)//2

    while metade > 0 and numeroDeAcoes > 0:
        for i in range(metade, len(lista)):
            valor = lista[i]
            j = i

            while j>= metade and lista[j - metade] > valor and numeroDeAcoes > 0:
                numeroDeAcoes -= 1
                if numeroDeAcoes > 0:
                    lista[j] = lista[j - metade]
                    j -= metade
                    numeroDeAcoes -= 1
            
            if j >= metade and numeroDeAcoes > 0:
                numeroDeAcoes -= 1
            lista[j] = valor
        
        metade = metade//2
    
    return lista

# Antes de chamar a função, deve pegar a variavel vencedorAcoes e adicionar o valor dela ao
# acoesQuickSortLimitado -> acoesQuickSortLimitado = vencedorAcoes
# demonstração logo abaixo de como seria chamado:
# toninhoNovo = sequencia.split()
# acoesQuickSortLimitado = vencedorAcoes
# quickSortLimitado(toninhoNovo)
# print(f"Com {vencedorAcoes} ações, Toninho ordena a lista assim: {toninhoNovo}")

acoesQuickSortLimitado = 0
def quickSortLimitado(A, lo=0, hi=None):
    # criando uma lista fantasma para não atrapalhar as outras funções
    for i in range(len(A)):
        A[i] = int(A[i])
    
    if hi == None:
        hi = len(A) - 1
    if lo >= 0 and hi >= 0 and lo < hi and acoesQuickSortLimitado > 0:
        print("opa", acoesQuickSortLimitado)
        p = partitionLimitado(A, lo, hi)
        quickSortLimitado(A, lo, p)
        quickSortLimitado(A, p + 1, hi)

def partitionLimitado(A, lo, hi):
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    global acoesQuickSortLimitado
    while True and acoesQuickSortLimitado > 0:
        if i >= j:
            return j
        while A[i] < pivot and acoesQuickSortLimitado > 0:
            acoesQuickSortLimitado -= 1
            i += 1
        while A[j] > pivot and acoesQuickSortLimitado > 0:
            acoesQuickSortLimitado -= 1
            j -= 1

        if i!=j:
            acoesQuickSortLimitado -= 1 
            A[i], A[j] = A[j], A[i]

    return i

listaNomeAcoes = [1, 2, 3, 4, 5]
# a lista acima foi feita pensando em otimizar ao evitar o uso da função append

listabubbleSort = sequencia.split()
cacaRato = bubbleSort(listabubbleSort)
print(f"Caça-Rato ordena a lista com {cacaRato[0]} comparações e {cacaRato[1]} trocas.")
totalCacaRato = cacaRato[0] + cacaRato[1]
listaNomeAcoes[0] = [totalCacaRato, "Caça-Rato"]

listaselectionSort = sequencia.split()
grafite = selectionSort(listaselectionSort)
print(f"Grafite ordena a lista com {grafite[0]} comparações e {grafite[1]} trocas.")
totalGrafite = grafite[0] + grafite[1]
listaNomeAcoes[1] = [totalGrafite, "Grafite"]

listainsertionSort = sequencia.split()
lacraia = insertionSort(listainsertionSort)
print(f"Lacraia ordena a lista com {lacraia[0]} comparações e {lacraia[1]} trocas.")
totalLacraia = lacraia[0] + lacraia[1]
listaNomeAcoes[2] = [totalLacraia, "Lacraia"]

listashellSort = sequencia.split()
rivaldo = shellSort(listashellSort)
print(f"Rivaldo ordena a lista com {rivaldo[0]} comparações e {rivaldo[1]} trocas.")
totalRivaldo = rivaldo[0] + rivaldo[1]
listaNomeAcoes[3] = [totalRivaldo, "Rivaldo"]

listaquickSort = sequencia.split()
toninho = quickSort(listaquickSort)
print(f"Toninho ordena a lista com {numeroCompQuick} comparações e {numeroTrocaQuick} trocas.")
totalToninho = numeroCompQuick + numeroTrocaQuick
listaNomeAcoes[4] = [totalToninho, "Toninho"]

print("-VENCEDOR DA RODADA-")

vencedor = listaNomeAcoes[0][1]
vencedorAcoes = listaNomeAcoes[0][0]
for i in listaNomeAcoes:
    if i[0] < vencedorAcoes:
        vencedor = i[1]
        vencedorAcoes = i[0]

print(f"O vencedor da rodada é {vencedor}, com {vencedorAcoes} ações.")
print("-Toninho está a dormir...-")
print("Os outros estagiários retornam as seguintes listas com essa quantidade de ações:")

if vencedor == "Caça-Rato":
    listaselectionSortLimitada = sequencia.split()
    grafiteNovo = selectionSortLimitado(listaselectionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Grafite ordena a lista assim: {grafiteNovo}")

    listainsertionSortLimitada = sequencia.split()
    lacraiaNovo = insertionSortLimitado(listainsertionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Lacraia ordena a lista assim: {lacraiaNovo}")

    listashellSortLimitada = sequencia.split()
    rivaldoNovo = shellSortLimitado(listashellSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Grafite ordena a lista assim: {grafiteNovo}")

elif vencedor == "Grafite":
    listabubbleSortLimitada = sequencia.split()
    cacaRatoNovo = bubbleSortLimitado(listabubbleSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Caça-Rato ordena a lista assim: {cacaRatoNovo}")

    listainsertionSortLimitada = sequencia.split()
    lacraiaNovo = insertionSortLimitado(listainsertionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Lacraia ordena a lista assim: {lacraiaNovo}")

    listashellSortLimitada = sequencia.split()
    rivaldoNovo = shellSortLimitado(listashellSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Rivaldo ordena a lista assim: {rivaldoNovo}")

elif vencedor == "Lacraia":
    listabubbleSortLimitada = sequencia.split()
    cacaRatoNovo = bubbleSortLimitado(listabubbleSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Caça-Rato ordena a lista assim: {cacaRatoNovo}")

    listaselectionSortLimitada = sequencia.split()
    grafiteNovo = selectionSortLimitado(listaselectionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Grafite ordena a lista assim: {grafiteNovo}")

    listashellSortLimitada = sequencia.split()
    rivaldoNovo = shellSortLimitado(listashellSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Rivaldo ordena a lista assim: {rivaldoNovo}")

elif vencedor == "Rivaldo":
    listabubbleSortLimitada = sequencia.split()
    cacaRatoNovo = bubbleSortLimitado(listabubbleSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Caça-Rato ordena a lista assim: {cacaRatoNovo}")

    listaselectionSortLimitada = sequencia.split()
    grafiteNovo = selectionSortLimitado(listaselectionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes}, Grafite ordena a lista assim: {grafiteNovo}")

    listainsertionSortLimitada = sequencia.split()
    lacraiaNovo = insertionSortLimitado(listainsertionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Lacraia ordena a lista assim: {lacraiaNovo}")

else:
    listabubbleSortLimitada = sequencia.split()
    cacaRatoNovo = bubbleSortLimitado(listabubbleSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Caça-Rato ordena a lista assim: {cacaRatoNovo}")

    listaselectionSortLimitada = sequencia.split()
    grafiteNovo = selectionSortLimitado(listaselectionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Grafite ordena a lista assim: {grafiteNovo}")

    listainsertionSortLimitada = sequencia.split()
    lacraiaNovo = insertionSortLimitado(listainsertionSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Lacraia ordena a lista assim: {lacraiaNovo}")

    listashellSortLimitada = sequencia.split()
    rivaldoNovo = shellSortLimitado(listashellSortLimitada, vencedorAcoes)
    print(f"Com {vencedorAcoes} ações, Rivaldo ordena a lista assim: {rivaldoNovo}")
