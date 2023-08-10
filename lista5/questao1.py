class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] for i in range(vertices)]
    
    def adicionarSeguidores(self, v):
        usuario = int(v[0])
        seguidores = v[2:]
        self.grafo[usuario] = seguidores
        
    def imprimir(self):
        print(self.grafo)
    
    def bfs(self, vert, boost):
        visitados = [False] * self.vertices
        visitados[vert] = True
        # marcando o valor inicial como lido

        fila = [vert]
        lista = []
        while len(fila) > 0 and boost > 0:
            v = fila[0]
            for u in self.grafo[v]:
                u = int(u)
                if boost > 0:
                    if visitados[u] == False:
                        visitados[u] = True
                        lista.append(str(u))
                        fila.append(u)
                        if v!= vert:
                            boost -= 1
            fila.pop(0)
        
        return lista

numeroUsuarios = int(input())
idUsuario = int(input())
valorBoost = float(input())
boost = int(valorBoost//5.25)

grafo = Grafo(numeroUsuarios)
for i in range(numeroUsuarios):
    entrada = input().split()
    grafo.adicionarSeguidores(entrada)

lista = grafo.bfs(idUsuario, boost)
print(lista)
