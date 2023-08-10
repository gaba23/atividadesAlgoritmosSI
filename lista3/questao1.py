numeroEntradas = int(input())

class Tabela:
    def __init__(self):
        self.memoria = [None for i in range(11)]

    def inserir(self, dado):
        posicao = dado % 11

        if self.memoria[posicao] == None:
            self.memoria[posicao] = dado
        
        else:
            self.memoria[posicao] += dado
    
    def checagem(self, numeroMagico):
        permissao = False
        for i in range(11):
            if self.memoria[i] != None:
                for j in range(i, 11):
                    if self.memoria[j] != None and self.memoria[i]!=self.memoria[j]:
                        if self.memoria[i] + self.memoria[j] == numeroMagico:
                            permissao = True
        
        if permissao:
            print("UP Permission")
            
        else:
            print("NOT Permission")


while numeroEntradas > 0:
    numeroEntradas -= 1

    entrada = input().split()
    cpf = []
    for i in entrada[0]:
        cpf.append(int(i) * 10)
    
    cpfTabela = Tabela()
    for i in cpf:
        cpfTabela.inserir(i)
    
    cpfTabela.checagem(int(entrada[1]))