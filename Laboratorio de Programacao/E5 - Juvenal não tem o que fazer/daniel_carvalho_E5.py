def F(n):
    global counter
    if (n == 1):
        return 1, counter
    else:
        if (n % 2 == 0):
            counter += 1
            return F(n/2)
        else:
            counter += 1
            return F(3*n+1)
      
def G(n):
  F(n)
  global lista
  lista.append(counter)

import sys

arqentrada = open(sys.argv[1],"r")
arqsaida = open(sys.argv[2],"w")
casos = int(arqentrada.readline())
if (casos < 1) or (casos > 100):
    print("Valor de T fora da faixa aceitavel!")
else:
    listaCasos = []
    for i in range(1,casos+1):
        listaCasos.append(i)
    c = 0
    for linha in arqentrada:
        intervalo = []
        s = linha.split()
        n = list(map(int,s))
        sequencia =[x for x in range(n[0],n[1]+1)]
        lista = []
        counter = 0
        
        for i in sequencia:
            #global counter
            counter += 1
            G(i)
            counter = 0
        valor_max = max(lista)
        arqsaida.write("Caso %d: %d\n" % (listaCasos[c], valor_max))
        c += 1
arqentrada.close()
arqsaida.close()