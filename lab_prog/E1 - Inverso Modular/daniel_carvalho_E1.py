#Função de Cálculo do Inverso Modular#

import sys

arqentrada = open(sys.argv[1],"r")
arqsaida = open(sys.argv[2],"w")
t = int(arqentrada.readline())
if t<1 or t>1000:
    print("Valor de 'T' fora da faixa aceitável!")
else:
    flag = False
    lista = []
    for a in range(t):
        lista.append(a)
    c = 0
    for linha in arqentrada:
        s = linha.split()
        n = list(map(int,s))
        if n[0] < 1 or n[0] > 10000 or n[1] < 1 or n[1] > 1000:
            arqsaida.write("Valor(es) fora da faixa aceitável!\n")
        else:
            for i in range(n[1]):
                x = (n[0]*i)%n[1]
                if x == 1:
                    arqsaida.write("Caso %d: %d\n" % (lista[c],i))
                    flag = True
                    break
            if flag == False:
                arqsaida.write("Caso %d: muito dificil\n" % lista[c])
            flag = False
            c += 1
arqentrada.close()
arqsaida.close()
    
