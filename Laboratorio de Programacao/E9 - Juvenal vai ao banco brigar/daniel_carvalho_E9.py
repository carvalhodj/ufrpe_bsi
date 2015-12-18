import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None
    def getData(self):
        return self.data
    def setData(self, newData):
        self.data = newData
    def getNextNode(self):
        return self.nextNode
    def setNextNode(self, newNode):
        self.nextNode = newNode
    def getprevNode(self):
        return self.prevNode
    def setprevNode(self, newNode):
        self.prevNode = newNode

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._fim = None
    def isEmpty(self):
        return (self._inicio is None) or (self._fim is None)
    def inserirInicio(self, valor):
        newNode = Node(valor)
        if self.isEmpty():
            self._inicio = self._fim = newNode
        else:
            self._inicio.setprevNode = newNode
            newNode.setNextNode(self._inicio)
            newNode.setprevNode(None)
            self._inicio = newNode
    def inserirFim(self, valor):
        newNode = Node(valor)
        if self.isEmpty():
            self._inicio = self._fim = newNode
        else:
            self._fim.setNextNode(newNode)
            newNode.setprevNode(self._fim)
            newNode.setNextNode(None)
            self._fim = newNode
    def remover(self, valor):
        if self.isEmpty():
            return None
        currentNode = self._inicio
        while currentNode.getData() != valor:
            currentNode = currentNode.getNextNode()
            if currentNode == None:
                return "Valor nao encontrado!"
        if currentNode == self._inicio:
            temp = self._inicio.getNextNode()
            self._inicio.setNextNode(None)
            temp.setprevNode(None)
            self._inicio = temp
        elif currentNode == self._fim:
            temp = self._fim.getprevNode()
            self._fim.setprevNode(None)
            temp.setNextNode(None)
            self._fim = temp
        elif self._inicio == self._fim:
            self._inicio = self._fim = None
            return None
        else:
            temp = currentNode.getprevNode()
            temp2 = currentNode.getNextNode()
            temp2.setprevNode(temp)
            temp.setNextNode(temp2)
    def pesquisar(self, valor):
        if self.isEmpty():
            return 0
        currentNode = self._inicio
        while currentNode.getData() != valor:
            currentNode = currentNode.getNextNode()
            if currentNode == None:
                return "Valor nao encontrado!"
        return currentNode.getData()
    def imprimir(self):
        currentNode = self._inicio
        if self.isEmpty():
            return 0
        return currentNode.getData()
    def esvaziar(self):
        self._inicio = self._fim = None

class Fila(ListaEncadeada):
    def removeInicio(self):
        if self.isEmpty():
            return "Fila vazia!"
        else:
            valorPrimeiroNode = self._inicio.getData()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            else:
                temp = self._inicio.getNextNode()
                self._inicio.setNextNode(None)
                temp.setprevNode(None)
                self._inicio = temp

arqEntrada = open(sys.argv[1],"r")
arqSaida = open(sys.argv[2],"w")
nCasos = int(arqEntrada.readline())
for i in range(1, nCasos+1):
    arqSaida.write("Caso %d:\n" % i)
    qtdeCom = int(arqEntrada.readline())
    fila = Fila()
    filaPref = Fila()
    c = 0
    while (c < qtdeCom):
        x = (arqEntrada.readline()).split()
        if (len(x) > 1):
            x[1] = int(x[1])
        if (x[0] == 'f'):
            fila.inserirFim(x[1])
        elif (x[0] == 'p'):
            filaPref.inserirFim(x[1])
        elif (x[0] == 'A'):
            fila.removeInicio()
        elif (x[0] == 'B'):
            if filaPref.isEmpty():
                fila.removeInicio()
            else:
                filaPref.removeInicio()
        elif (x[0] == 'I'):
            fila1 = fila.imprimir()
            fila2 = filaPref.imprimir()
            arqSaida.write(str(fila1) +" "+ str(fila2)+"\n")
        c += 1
arqSaida.close()
arqEntrada.close()
    