def max_heapify(A,k):
    l = 2 * k + 1
    r = 2 * k + 2
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def pegarMinimo(lista):
    if len(lista) > 1:
        minimo = lista[1]
        for i in range(len(lista)//2, len(lista)):
          if lista[i] < minimo:
            minimo = lista[i]
    else:
        minimo = lista[0]
    return minimo

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)
        
lista = input().split()
constante = int(input())
for i in range(len(lista)):
    lista[i] = int(lista[i])

aux = 0
while len(lista) > 0:
    aux += 1
    n = len(lista)
    build_max_heap(lista)
    
    maior = lista[0]
    menor = pegarMinimo(lista)
    k = maior - (menor * constante)
    if k > 0:
        lista[0] = k
    else:
        lista.pop(0)

print(f"{aux} rodadas, partindo para a próxima!")
