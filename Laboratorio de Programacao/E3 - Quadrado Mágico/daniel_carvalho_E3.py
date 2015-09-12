import sys

arqentrada = open(sys.argv[1],"r")
arqsaida = open(sys.argv[2],"w")
ordem = int(arqentrada.readline())
if (ordem < 2) or (ordem > 10):
    print("Valor N fora da faixa aceitavel!")
else:
    matriz = []
    somaReferencia = 0
    somaLinha = 0
    somaColuna = 0
    somaDiagP = 0
    somaDiagS = 0
    flag = True
    flagAceite = True
    for linha in arqentrada:
        s = linha.split()
        n = list(map(int,s))
        matriz.append(n)
    for i in range(ordem):
        for j in range(ordem):
            if (matriz[i][j] < 0) or (matriz[i][j] > 1000):
                flagAceite = False
                break
    if (flagAceite == False):
        print("Valor fora da faixa aceitavel!")
    else:
        for i in range(ordem):
            somaReferencia += matriz[i][0]
        for i in range(ordem):
            somaLinha = 0
            for j in range(ordem):
                somaLinha += matriz[i][j]
            if(somaLinha != somaReferencia):
                flag = False
        for i in range(ordem):
            somaColuna = 0
            for j in range(ordem):
                somaColuna += matriz[j][i]
            if(somaColuna != somaReferencia):
                flag = False
        for i in range(ordem):
            somaDiagP += matriz[i][i]
        if(somaDiagP != somaReferencia):
            flag = False
        for i in range(ordem-1,-1,-1):
            somaDiagS += matriz[ordem-1-i][i]
        if(somaDiagS != somaReferencia):
            flag = False
        if(flag == True):
            arqsaida.write(str(somaReferencia)+"\n")
        else:
            arqsaida.write("-1\n")
arqentrada.close()
arqsaida.close()