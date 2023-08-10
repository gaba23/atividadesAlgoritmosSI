class Node:
    def __init__(self, data):
        self.data = data
        self.proximo = None
        self.anterior = None


class Fila:
    def __init__(self):
        self._primeiro = None
        self._ultimo = None
        self._tamanho = 0
    
    def inserir(self, elemento):
        node = Node(elemento)

        if self._tamanho == 0:
            self._ultimo = node
            self._primeiro = node
        else:
            aposOPrimeiro = self._primeiro.proximo
            penultimo = self._ultimo
            penultimo.proximo = node
            if self._primeiro == self._ultimo:
                self._primeiro.proximo = node
                node.anterior = self._primeiro
            self._ultimo = node
            self._ultimo.anterior = penultimo
        
        
        self._tamanho += 1
    
    def remover(self):
        if self._tamanho > 0:
            node = self._primeiro
            self._primeiro = self._primeiro.proximo
            self._tamanho -= 1
            if self._tamanho == 1:
                self._primeiro == None
                self._ultimo == None
            return node
    
    def retirarUltimo(self):
        node = self._ultimo
        self._ultimo = self._ultimo.anterior
        self._ultimo.proximo = None
        self._tamanho -= 1
        return node.data

    def imprimir(self):
        itemAtual = self._primeiro
        while itemAtual and aux<5:
            print(itemAtual.data)
            itemAtual = itemAtual.proximo
    
    def girarFila(self, recebedor):

        metadeDaFila = self._tamanho/2
        if self._tamanho % 2 == 0:
            while self._tamanho != metadeDaFila:
                recebedor.inserir(self._ultimo.data)
                self.retirarUltimo()
        else:
            while self._tamanho > metadeDaFila:
                recebedor.inserir(self._ultimo.data)
                self.retirarUltimo()            
        

caixa1 = Fila()
caixa2 = Fila()
totalCaixa1 = 0.0
totalCaixa2 = 0.0

entrada = input()
while entrada != "FIM":
    entrada = entrada.split()
    if entrada[0] == "ENTROU:":
        if int(entrada[2]) == 1:
            entrada[3] = float(entrada[3])
            entrada[3] = round(entrada[3], 2)
            caixa1.inserir([entrada[1], entrada[3]])
        else:
            entrada[3] = float(entrada[3])
            entrada[3] = round(entrada[3], 2)
            caixa2.inserir([entrada[1], entrada[3]])
        print(f"{entrada[1]} entrou na fila {entrada[2]}")
    
    else:
        if entrada[1] == "1":                     
            if caixa1._tamanho > 0:
                print(f"{caixa1._primeiro.data[0]} foi chamado para o caixa 1")
                totalCaixa1 += caixa1._primeiro.data[1]
                caixa1.remover()
            elif caixa1._tamanho == 0:
                caixa2.girarFila(caixa1)
                print(f"{caixa1._primeiro.data[0]} foi chamado para o caixa 1")
                totalCaixa1 += caixa1._primeiro.data[1]
                caixa1.remover()

        else:

            if caixa2._tamanho > 0:
                print(f"{caixa2._primeiro.data[0]} foi chamado para o caixa 2")
                totalCaixa2 += caixa2._primeiro.data[1]
                caixa2.remover()
            elif caixa2._tamanho == 0:
                caixa1.girarFila(caixa2)
                atendente = caixa2._primeiro
                print(f"{atendente.data[0]} foi chamado para o caixa 2")
                totalCaixa2 += caixa2._primeiro.data[1]
                caixa2.remover()

    entrada = input()
    if entrada == "FIM":
      print(f"Caixa 1: R$ {totalCaixa1:.2f}, Caixa 2: R$ {totalCaixa2:.2f}")