def mergeSort(lista):
    if len(lista) > 1:

        #  dividindo a lista na metade
        meio = len(lista)//2
        primeiraMetade = lista[:meio]
        segundaMetade = lista[meio:]

        # realiza o mergeSort com cada uma delas
        mergeSort(primeiraMetade)
        mergeSort(segundaMetade)

        i = 0
        j = 0
        indice = 0

        # Comparação dos itens de cada metade para checar qual é menor
        while i < len(primeiraMetade) and j < len(segundaMetade):
            if primeiraMetade[i] < segundaMetade[j]:
                # caso o valor da esquerda seja menor que o da direita, irá ocupar uma posição anterior
                lista[indice] = primeiraMetade[i]
                i += 1
            else:
                # caso em que o item da direita é menor
                lista[indice] = segundaMetade[j]
                j += 1
            indice += 1

        # caso a lista da direita ou da esquerda se encerre, será inserido os itens da lista restante
        while i < len(primeiraMetade):
            lista[indice] = primeiraMetade[i]
            i += 1
            indice += 1

        while j < len(segundaMetade):
            lista[indice] = segundaMetade[j]
            j += 1
            indice += 1

salariosSport = input().split()
salariosBahia = input().split()
salarios = salariosSport + salariosBahia

for i in range(len(salarios)):
    salarios[i] = int(salarios[i])

mergeSort(salarios)

n = len(salarios)
if n%2 != 0:
    aux = int(n//2)
    mediana = salarios[aux]
else:
    aux = int(n/2)
    mediana = (salarios[aux - 1] + salarios[aux])/2

print(f"O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais.")
