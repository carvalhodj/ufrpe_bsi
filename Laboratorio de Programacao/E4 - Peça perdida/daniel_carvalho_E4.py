import sys

arqentrada = open(sys.argv[1],"r")
arqsaida = open(sys.argv[2],"w")
n = int(arqentrada.readline())
if (n < 2) or (n > 1000):
    print("Valor N fora da faixa aceitavel!")
else:
    seqOrig = []
    somaOrig = 0
    somaF = 0
    dif = 0
    for i in range(1,n+1):
        seqOrig.append(i)
    listaF = (arqentrada.readline()).split()
    listaF = (list(map(int, listaF)))
    for i in seqOrig:
        somaOrig += i
    for j in listaF:
        somaF += j
    if (somaOrig != somaF):
        dif = somaOrig - somaF
        arqsaida.write(str(dif)+"\n")
    else:
        print("Nao ha peca perdida")
arqentrada.close()
arqsaida.close()