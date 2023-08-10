class Node:
    def __init__(self, data):
        self.data = data
        self.direita = None
        self.esquerda = None

class Arvore:
    def __init__(self):
        self.tamanho = 0
        self.primeiro = None
        self.ultimo = None
        self.texto = ""
    
    def inserir(self, item):
        item = Node(item)
        if self.tamanho == 0:
            self.primeiro = item
            self.ultimo = item
        
        elif self.tamanho == 1:
            if self.primeiro.data > item.data:
                primeiroAntigo = self.primeiro
                self.primeiro = item
                item.direita = primeiroAntigo
                primeiroAntigo.esquerda = item
            else:
                self.ultimo = item
                item.esquerda = self.primeiro
                self.primeiro.direita = item 
        
        else:
            itemAtual = self.primeiro
            naoEntrou = True
            while itemAtual and naoEntrou:
                if itemAtual.data > item.data:
                    if itemAtual.data == self.primeiro.data:
                        self.primeiro = item
                        item.direita = itemAtual
                        itemAtual.esquerda = item
                    else:
                        esquerda = itemAtual.esquerda
                        esquerda.direita = item
                        item.esquerda = esquerda
                        item.direita = itemAtual
                        itemAtual.esquerda = item
                    naoEntrou = False
                itemAtual = itemAtual.direita
            if self.ultimo.data < item.data:
              self.ultimo.direita = item
              item.esquerda = self.ultimo
              self.ultimo = item
        
        self.tamanho += 1
        print(f"{item.data} INSERIDO")
            


    
    def deletar(self, valor):
        item = valor[0]
        if self.tamanho == 0:
            print(f"{item} NAO ENCONTRADO")
        
        else:
          naoEncontrado = True
          if item == self.primeiro.data:
              if self.tamanho == 1:
                  self.primeiro = None
                  self.ultimo = None
                  naoEncontrado = False
  
              else:
                  segundo = self.primeiro.direita
                  segundo.esquerda = None
                  self.primeiro = segundo
                  naoEncontrado = False

          
          elif item == self.ultimo.data:
              penultimo = self.ultimo.esquerda
              penultimo.direita = None
              self.ultimo = penultimo
              naoEncontrado = False

  
          else:
              itemAtual = self.primeiro
              while itemAtual and naoEncontrado:
                  if itemAtual.data == item:
                      esquerda = itemAtual.esquerda
                      direita = itemAtual.direita
                      esquerda.direita = direita
                      direita.esquerda = esquerda
                      naoEncontrado = False

                  else:
                      itemAtual = itemAtual.direita
          if naoEncontrado:
            print(f"{item} NAO ENCONTRADO")
          else:
            self.tamanho -= 1
            print(f"{item} DELETADO")
      
    def imprimir(self):
        itemAtual = self.primeiro
        while itemAtual:
            if itemAtual == self.primeiro:
              self.texto = itemAtual.data
            else:
              self.texto = self.texto + " " + itemAtual.data
            itemAtual = itemAtual.direita
        print(self.texto)
    
    def imprimirAPartir(self, item):
      itemAtual = self.primeiro
      
      while itemAtual and itemAtual.data != item:
        itemAtual = itemAtual.direita
      
      if itemAtual == None:
        print(f"{item} NAO ENCONTRADO")
        
      else:
        while itemAtual:
            if itemAtual == self.primeiro:
              self.texto = itemAtual.data
            else:
              self.texto = self.texto + " " + itemAtual.data
            itemAtual = itemAtual.direita
        print(self.texto)
        


arvore = Arvore()
entrada = input()
while entrada != "FIM":
  entrada = entrada.split()
    
  if entrada[0] == "INSERIR":
    arvore.inserir(entrada[1])
    
  elif entrada[0] == "DELETAR":
    arvore.deletar([entrada[1]])
    
  elif entrada[0] == "MINIMO":
    if arvore.tamanho == 0:
      print("ARVORE VAZIA")
    else:
      print(f"MENOR: {arvore.primeiro.data}")
    
  elif entrada[0] == "MAXIMO":
    if arvore.tamanho == 0:
      print("ARVORE VAZIA")
    else:
      print(f"MAIOR: {arvore.ultimo.data}")
    
  elif entrada[0] == "VER" and len(entrada) > 1:
    if arvore.tamanho == 0:
      print("ARVORE VAZIA")
    else:
      arvore.imprimirAPartir(entrada[1])
    
  elif entrada[0] == "VER":        
    if arvore.tamanho == 0:
      print("ARVORE VAZIA")
    else:
      arvore.imprimir()
  else:
    tamanho = arvore.tamanho
    aux = 1
    altura = 0
    aux2 = True
    while aux2:
      if 2**aux > tamanho:
        altura = aux
        aux2 = False
      else:
        aux += 1
    print(f"ALTURA: {altura}")

  entrada = input()

if arvore.tamanho == 0:
  print("ARVORE VAZIA")
else:
  arvore.imprimir()