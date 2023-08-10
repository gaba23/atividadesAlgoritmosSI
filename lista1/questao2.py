ordemDasCapas = input()
listaDeFrentes = []
listaDeVersos = []
deuErro = False
for i in range(len(ordemDasCapas)):
    if ordemDasCapas[i] == "F":
        listaDeFrentes.append([ordemDasCapas[i], i + 1])
    else:
        listaDeVersos.append(ordemDasCapas[i])
        if len(listaDeVersos) > len(listaDeFrentes):
            print(f"Incorreto, devido a capa na posição {i + 1}.")
            deuErro = True

if len(listaDeFrentes) > len(listaDeVersos):
    print(f"Incorreto, devido a capa na posição {listaDeFrentes[len(listaDeVersos)][1]}.")
    deuErro = True

if not deuErro:
    print("Correto.")