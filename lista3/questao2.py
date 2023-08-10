qtdEspaco = int(input())
qtdChamadas = int(input())

class Tabela:
  def __init__(self):
    self.qtdMemoria = qtdEspaco
    self.memoria = [[] for i in range(qtdChamadas)]
  
  def inserir(self, dado):
    posicaoDado = dado % qtdEspaco
    
    if self.memoria[posicaoDado] == []:
        self.memoria[posicaoDado].append(dado)
    
    else:
        naoEntrou = True
        aux = 1
        while naoEntrou:
            posicaoDado = (dado + aux) % qtdEspaco
            if self.memoria[posicaoDado] == []:
                self.memoria[posicaoDado].append(dado)
                naoEntrou = False
            else:
                aux += 1
        
    print(f"E: {posicaoDado}")

    self.checagem()
  
  def procurarDado(self, dado):
    encontrado = False
    for i in range(len(self.memoria)):
      if len(self.memoria[i]) == 1:
        if self.memoria[i][0] == dado:  
          encontrado = True
          print(f"E: {i}") 
    if encontrado == False:
      print("NE")

  
  def procurarMemoria(self, memoria):
    dadoEncontrado = self.memoria[memoria]
    if dadoEncontrado == []:
      print("D")
    else:
      print(f"A: {self.memoria[memoria][0]}")
      
  def checagem(self):
    memoriaCheia = True
    for i in self.memoria:  
      if i == []:
        memoriaCheia = False
    if memoriaCheia == True:
      print("Toda memoria utilizada")
      qtdChamadas = 0

tabela = Tabela()

while qtdChamadas>0:
  qtdChamadas -= 1
  
  entrada = input()
  entrada = entrada.split()
  
  if entrada[0] == "ADD":
    tabela.inserir(int(entrada[1]))
  
  elif entrada[0] == "CAP":
    tabela.procurarMemoria(int(entrada[1]))
  
  else:
    tabela.procurarDado(int(entrada[1]))