import sys

def selectionDecresc(lista):
    n = len(lista)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if (lista[j] > lista[mini]):
                mini = j
        lista[i],lista[mini]=lista[mini],lista[i]
    return lista
def selectionCresc(lista):
    n = len(lista)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if (lista[j] < lista[mini]):
                mini = j
        lista[i],lista[mini]=lista[mini],lista[i]
    return lista

arqentrada = open(sys.argv[1], "r")
arqsaida = open(sys.argv[2], "w")
linha1 = (arqentrada.readline()).split()
qtdeAlunos = int(linha1[0])
qtdeTimes = int(linha1[1])
c = 0
listaAlunos = []
while c < qtdeAlunos:
    x = (arqentrada.readline()).split()
    x[1] = int(x[1])
    x[0], x[1] = x[1], x[0]
    listaAlunos.append(x)
    c += 1
selectionDecresc(listaAlunos)
for i in range(1,qtdeTimes+1):
    listaTemp = []
    k = 0
    arqsaida.write("Time %d\n" % i)
    for j in range(i-1,len(listaAlunos),qtdeTimes):
        listaTemp.append(listaAlunos[j][1])
    selectionCresc(listaTemp)
    for l in range(len(listaTemp)):
        arqsaida.write(listaTemp[l]+"\n")
    arqsaida.write("\n")
arqentrada.close()
arqsaida.close()
