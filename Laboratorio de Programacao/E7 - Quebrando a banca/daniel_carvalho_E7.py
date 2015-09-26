import sys

arqEntrada = open(sys.argv[1], "r")
arqSaida = open(sys.argv[2], "w")
while True:
    line1 = arqEntrada.readline()
    if line1 == '':
        break
    line1 = line1.split()
    line1 = list(map(int, line1))
    line2 = int(arqEntrada.readline())
    line2 = list(map(int, str(line2)))
    listaSaldo = line2[:]
    for i in range(line1[1]):
        listaSaldo.remove(min(listaSaldo))
    for i in listaSaldo:
        arqSaida.write(str(i))
    arqSaida.write("\n")
arqEntrada.close()
arqSaida.close()