class Node:
    def __init__(self, data):
        self.data = data
        self.pai = None
        self.filho1 = None
        self.filho2 = None
        self.posicao = None
        self.proximo = None
        self.anterior = None

class Arvore:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        self.piso = 1

    def inserir(self, data):
        node = Node(data)
        if self.tamanho == 0:
            self.primeiro = node
            node.posicao = 0
            self.tamanho += 1
            self.ultimo = node
        
        else:
            self.tamanho += 1
            adicionado = False
            itemAtual = self.primeiro
            vistoAmbos = False
            while not adicionado:
   
                if int(node.data) > int(itemAtual.data):
                    if itemAtual.filho2 == None:
                        itemAtual.filho2 = node
                        node.pai = itemAtual
                        self.ultimo.proximo = node
                        node.anterior = self.ultimo
                        self.ultimo = node
                        adicionado = True
                        node.posicao = itemAtual.posicao + 1
                    else:
                        itemAtual = itemAtual.filho2
                        
                else:
                    if itemAtual.filho1 == None:
                        itemAtual.filho1 = node
                        node.pai = itemAtual
                        self.ultimo.proximo = node
                        node.anterior = self.ultimo
                        self.ultimo = node
                        adicionado = True
                        node.posicao = itemAtual.posicao + 1
                    else:
                        itemAtual = itemAtual.filho1

        print(node.posicao)
    
    def procurar(self, item):
        itemAtual = self.primeiro
        encontrado = False
        while itemAtual:
            if itemAtual.data == item:
                encontrado = True
                print(itemAtual.posicao)
                aux = 1
                
                if itemAtual == self.primeiro:
                    pass
                
                else:
                  
                    if itemAtual == self.ultimo:
                      penultimo = itemAtual.anterior
                      self.ultimo = penultimo
                    
                    self.ultimo.proximo = None
                  
                    itemSequencia = self.primeiro
                    itemAtual.filho1 = None
                    itemAtual.filho2 = None
                    anterior = itemAtual.anterior
                    proximo = itemAtual.proximo                    
                    
                    if self.tamanho == 2:
                        self.primeiro.proximo = None
                        self.ultimo.anterior = None
                    
                    else:
                        if proximo != None:
                            anterior.proximo = proximo
                            proximo.anterior = anterior
                        else:
                            anterior.proximo = None
                    itemAtual.proximo = self.primeiro
                    itemAtual.anterior = None
                    self.primeiro = itemAtual
                    itemAtual.posicao = 0
                    
                    novaPosicao = 1
                    
                    if itemAtual == self.ultimo:
                      self.ultimo
                    
                    while itemSequencia != None:
                        itemSequencia.filho1 = None
                        itemSequencia.filho2 = None
   
                        if int(itemSequencia.data) < int(itemAtual.data):
                            
                            if itemAtual.filho1 == None:
                                itemAtual.filho1 = itemSequencia
                                itemSequencia.pai = itemAtual
                                itemSequencia.posicao = itemAtual.posicao + 1
                                itemSequencia = itemSequencia.proximo
                            
                            else:
                                itemAtual = itemAtual.filho1
                
                        else:
                            
                            if itemAtual.filho2 == None:
                                itemAtual.filho2 = itemSequencia
                                itemSequencia.pai = itemAtual
                                itemSequencia.posicao = itemAtual.posicao + 1
                                itemSequencia = itemSequencia.proximo
                                
                            else:
                                itemAtual = itemAtual.filho2                                                   
                break
            else:
                itemAtual = itemAtual.proximo
        if encontrado == False:
            print(-1)

    def imprimir(self):
        item = self.primeiro
        while item:
            
            print(item.posicao)
            item = item.proximo


arvore = Arvore()
entrada = input()
try:
  while entrada:
    entrada = entrada.split()
    if entrada [0] == "ADD":
      arvore.inserir(entrada[1])
    else:
      arvore.procurar(entrada[1])
    entrada = input()
except:
    pass                      


