class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        # criando a matriz com cada valor sem conexões prévias
    
    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1
        # adicionando a conexão tanto entre "u" e "v" quanto para "v" e "u"
    
    def bfs(self, v):
        
        visitados = [False] * self.vertices
        visitados[v - 1] = True
        # marcando o valor inicial como lido

        fila = [v - 1]
        alcancados = 1

        while len(fila) > 0:
            v = fila[0]
            for u in range(self.vertices):
                if self.grafo[v][u] == 1:
                    if visitados[u] == False:

                        visitados[u] = True
                        fila.append(u)
                        alcancados += 1
            fila.pop(0)
        
        return alcancados

entrada1 = input().split()
grafo = Grafo(int(entrada1[0]))

for i in range(int(entrada1[1])):
    entrada = input().split()
    grafo.add_aresta(int(entrada[0]), int(entrada[1]))

for i in range(1, int(entrada1[0]) + 1):
    aux = str(grafo.bfs(i))
    if i == 1:
        alcancadosLista = aux
    else:
        alcancadosLista = alcancadosLista + " " + aux

print(alcancadosLista)
