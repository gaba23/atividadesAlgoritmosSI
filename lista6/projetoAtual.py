from tkinter import *

arquivo = open("lemis.gml", "r")

class Grafo:
 
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0] * vertices] * vertices
        self.arestasGrafo = []
 
    # adição das arestas ao grafo
    def adicionarAresta(self, u, v, w):
        self.arestasGrafo.append([u, v, w])
        self.arestasGrafo.append([v, u, w])
        self.grafo[u][v] = w
        self.grafo[v][u] = w
         
    def imprimir(self):
        print(self.grafo) 

    def BellmanFord(self, inicio, fim):
 
        # Criação de uma lista que vai armazenar as distâncias entre o vertíce inicial e todos os outros
        dist = [float("Inf")] * self.V
        
        # Distância do vértice inicial começando em 0 e os restantes em infinito
        dist[inicio] = 0

        # Criação da listas que define o antecessor de cada vértice
        antecessor = [-1] * self.V
 
        # Relaxamento dos vértices em (vértices - 1) vezes
        for i in range(self.V - 1):
            for aresta in self.arestasGrafo:
            # Atualização do valor da distância de cada aresta
                u = aresta[0]
                v = aresta[1]
                peso = aresta[2]

                if dist[u] != float("Inf") and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    antecessor[v] = (u, peso)
 
        # Checagem final, para ver se o grafo tem um ciclo negativo
        for aresta in self.arestasGrafo:
                u = aresta[0]
                v = aresta[1]
                peso = aresta[2]
                if dist[u] != float("Inf") and dist[u] + peso < dist[v]:
                        print("O grafo contém um ciclo negativo")
                        return

        return dist, antecessor
aux = 0
titulos = []
for linha in arquivo:
    dados = linha.split()
    if aux == 0:
        # Checagem se é a primeira linha, a qual tem o número de vertices e arestas, para ser criado o grafo
        numVertices = int(dados[0])
        grafo = Grafo(numVertices)
        aux = 1
    
    elif dados[0] == "label":
        titulos.append(dados[1])

    else:
        # Checagem para ver se a linha atual é a que informa uma aresta
        if len(dados) > 2 and dados[0] != "Creator":
            grafo.adicionarAresta(int(dados[0]), int(dados[1]), int(dados[2]))


janela = Tk()
janela.title("Projeto Algoritmos - Gabriel Alves")

textoInicio = Label(janela, text="Insira o valor do vértice inicial e final para realizar o algoritmo Bellman-Ford.")
textoInicio.grid(column=2, row=0)

textoInicio2 = Label(janela, text="O primeiro vértice é o 0 e o último o 90.")
textoInicio2.grid(column = 2, row=1)

labelVerticeInicial = Label(janela, text="Insira o vértice inicial:")
labelVerticeInicial.grid(column = 0, row= 4)
verticeInicial = Entry(janela, width=5)
verticeInicial.grid(column=0, row= 5)

labelVerticeFinal = Label(janela, text ="Insira o vértice final:")
labelVerticeFinal.grid(column = 3, row = 4)
verticeFinal = Entry(janela, width =5)
verticeFinal.grid(column = 3, row = 5)

# Criando as labels com texto em vazio para manipulação no futuro, possibilitando a realização do cálculo em mais de uma vez
label1 = Label(janela, text = "")
label1.grid(column=2, row= 8)

label2 = Label(janela, text="")
label2.grid(column=2, row= 9)

label3 = Label(janela, text = "")
label3.grid(column=2, row= 10)

def bellmanFord():
    # Resetando o texto para uma nova análise
    label1.configure(text = "")
    label2.configure(text = "")
    label3.configure(text = "")

    valorInicial = verticeInicial.get()
    valorFinal = verticeFinal.get()

    if valorInicial == "" or valorFinal == "":
        pass
    elif int(valorInicial) < numVertices and int(valorInicial) >= 0 and int(valorFinal) < numVertices and int(valorFinal) >= 0:

        listas = grafo.BellmanFord(int(valorInicial), int(valorFinal))
        dist = listas[0]
        antecessor= listas[1]
        inicio = int(valorInicial)
        fim = int(valorFinal)

        if dist[fim] == float("Inf"):
            # Checagem se não existe um caminho entre os vértices
            label1.configure(text = "Não existe um caminho entre os vértices " + str(titulos[inicio]) + " e " + str(titulos[fim]))

        else:
            # O caminho existe, então partimos para os dados
            label1.configure( text = "O peso entre os vértices " + str(titulos[inicio]) + " e " +  str(titulos[fim]) + " é " + str(dist[fim]))

            atual = fim
            texto = 'Caminho feito:'
            texto2 = 'Pesos:'
            caminho = []
            peso = []
            while antecessor[atual] != -1:
                # Pegando o caminho através do antecessor de cada vértice, até o inicial
                caminho.append(antecessor[atual][0])
                peso.append(antecessor[atual][1])
                atual = antecessor[atual][0]
            
            for i in range(len(caminho) -1, -1, -1):
                # Usei um for que diminui para pegar do inicial até o final, já que a adição no while foi de trás pra frente tendo em vista q eu fui pelo filho de cada vértice
                texto = texto + " " + titulos[caminho[i]] + "(" + str(caminho[i]) + ")"
                texto2 = texto2 + " " + str(peso[i])

            texto += " " + titulos[fim] + "(" + str(fim) + ")"

            label2.configure(text = texto)

            label3.configure(text = texto2)
    

botao = Button(janela, text="inicie a função", command=bellmanFord)
botao.grid(column=3, row= 6)

#grafo.BellmanFord(valorInicial, valorFinal)

janela.geometry("800x400")
janela.mainloop()
