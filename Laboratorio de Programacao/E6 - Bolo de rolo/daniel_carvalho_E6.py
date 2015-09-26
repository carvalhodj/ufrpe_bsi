import sys

arqEntrada = open(sys.argv[1], "r")
arqSaida = open(sys.argv[2], "w")
def contagem(a,b):
    c = 0
    for i in range(a):
        c += tamanhoBolos[i]//b
    return c
def verificacao(x,y,z):
    return contagem(x,y) >= z
qtdePessoas = arqEntrada.readline()
qtdePessoas = int(qtdePessoas)
qtdeBolos = arqEntrada.readline()
qtdeBolos = int(qtdeBolos)
tamanhoBolos = arqEntrada.readline().split()
tamanhoBolos = list(map(int, tamanhoBolos))
maior = max(tamanhoBolos)
menor = 1
s = 0
while (menor <= maior):
    m = menor + (maior-menor)//2
    p = contagem(qtdeBolos,m)
    if verificacao(qtdeBolos,m,qtdePessoas):
        menor = m+1
        s = m
    else:
        maior = m-1
arqSaida.write(str(s)+"\n")
arqEntrada.close()
arqSaida.close()

