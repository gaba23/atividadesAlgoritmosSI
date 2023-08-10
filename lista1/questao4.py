class ControleNo:
    def __init__(self, data):
        self.data = data
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self._primeiro = None
        self._ultimo = None

    def inserir(self, conteudo):
        item = ControleNo(conteudo)
        if self._primeiro == None:
            self._primeiro = item
            self._ultimo = item

        else:
            segundo = self._primeiro
            self._primeiro = item
            item.proximo = segundo
            segundo.anterior = item

    def remover(self, item):
        if self._primeiro.data == item:
            self._primeiro = self._primeiro.proximo
            self._primeiro.anterior = None
        elif self._ultimo.data == item:
            self._ultimo = self._ultimo.anterior
            self._ultimo.proximo = None
        else:
          itemAtual = self._primeiro
          while item != itemAtual.data:
            itemAtual = itemAtual.proximo
          
          itemApos = itemAtual.proximo
          itemAntes = itemAtual.anterior
          itemApos.anterior = itemAntes
          itemAntes.proximo = itemApos
            
          
    def moverProInicio(self, conteudo):
      self.remover(conteudo)
      self.inserir(conteudo)

    def imprimir(self):
        itemAtual = self._primeiro
        while itemAtual:
            print(itemAtual.data)
            itemAtual = itemAtual.proximo

lista = Lista()
entrada = input()
while entrada != "END":
  entrada = entrada.split()
  if entrada[0] == "ADD":
    lista.inserir(entrada[1])
  elif entrada[0] == "FIND":
    lista.moverProInicio(entrada[1])
  elif entrada[0] == "REM":
    lista.remover(entrada[1])
  else:
    lista.imprimir()
  entrada = input()