# Programa de Detecção de Colisão entre retângulos #

import sys

arqentrada = open(sys.argv[1],"r")
arqsaida = open(sys.argv[2],"w")
c = []
retA = []
retB = []
for linha in arqentrada:
  s = linha.split()
  n = list(map(int,s))
  for i in n:
    c.append(i)
for i in range(4):
  retA.append(c[i])
for j in range(4,8):
  retB.append(c[j])
wA = abs(retA[2] - retA[0])
wB = abs(retB[2] - retB[0])
hA = abs(retA[3] - retA[1])
hB = abs(retB[3] - retB[1])
if ((retA[0] < 0) or (retB[0] < 0) or (retA[0] > retA[2]) or (retB[0] > retB[2]) or (retA[2] < 0) or (retB[2] < 0)):
  print("X0 ou X1 com valor inválido!\n")
elif ((retA[0] > 1000000) or (retB[0] > 1000000) or (retA[2] > 1000000) or (retB[2] > 1000000)):
  print("X0 ou X1 com valor inválido!\n")
elif ((retA[1] < 0) or (retB[1] < 0) or (retA[1] > retA[3]) or (retB[1] > retB[3]) or (retA[3] < 0) or (retB[3] < 0)):
  print("Y0 ou Y1 com valor inválido!\n")
elif ((retA[1] > 1000000) or (retB[1] > 1000000) or (retA[3] > 1000000) or (retB[3] > 1000000)):
  print("Y0 ou Y1 com valor inválido!\n")
elif ((retA[0]+ wA < retB[0]) or (retA[0] > retB[0] + wB)):
  arqsaida.write("0")
elif ((retA[1] + hA < retB[1]) or (retA[1] > retB[1] + hB)):
  arqsaida.write("0")
else:
  arqsaida.write("1")
arqentrada.close()
arqsaida.close()
