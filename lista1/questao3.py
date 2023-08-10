pilha = input().split(",")
anterior = int(pilha[0])
caos = False

for i in pilha:
  if anterior > int(i):
    caos = True
  anterior = int(i)
entrada2 = input()
if caos:
  print("A pilha está um caos.")
else:
  for i in range(len(pilha)):
    if int(entrada2) < int(pilha[i]) and entrada2 not in pilha:
      pilha.insert(i, entrada2)
  print(pilha)