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
    def getData(self):
        return self._inicio
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
            return None
        currentNode = self._inicio
        while currentNode.getData() != valor:
            currentNode = currentNode.getNextNode()
            if currentNode == None:
                return None
        return currentNode.getData()
    def imprimir(self):
        currentNode = self._inicio
        if self.isEmpty():
            print("Lista vazia")
        while currentNode != None:
            print(currentNode.getData())
            currentNode = currentNode.getNextNode()
    def esvaziar(self):
        self._inicio = self._fim = None
    def removeFim(self):
        if self.isEmpty():
            return None
        else:
            valorUltimoNode = self._fim.getData()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            else:
                temp = self._fim.getprevNode()
                self._fim.setprevNode(None)
                temp.setNextNode(None)
                self._fim = temp
            return valorUltimoNode

class Fila(ListaEncadeada):
    def removeInicio(self):
        if self.isEmpty():
            return None
        else:
            valorPrimeiroNode = self._inicio.getData()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            else:
                temp = self._inicio.getNextNode()
                self._inicio.setNextNode(None)
                temp.setprevNode(None)
                self._inicio = temp
            return valorPrimeiroNode

class Pilha(ListaEncadeada):
    def removeFim(self):
        if self.isEmpty():
            return None
        else:
            valorUltimoNode = self._fim.getData()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            else:
                temp = self._fim.getprevNode()
                self._fim.setprevNode(None)
                temp.setNextNode(None)
                self._fim = temp
            return valorUltimoNode

arqEntrada = open(sys.argv[1], "r")
arqSaida = open(sys.argv[2], "w")
nFestas = int(arqEntrada.readline())
for i in range(1,nFestas+1):
    deckMesa = (arqEntrada.readline()).split()
    cartasMesa = Fila()
    cartasMesa.inserirFim(deckMesa)
    filas = Fila()
    deck = None
    c = 1
    while True:
        deck = (arqEntrada.readline()).split()
        if (deck == ["-1"]):
            break
        filas.inserirFim(deck)
        c += 1
    rodadas = 1000
    juvenal = True
    tmp = c
    while rodadas > 0:
        c = tmp
        x = cartasMesa.removeInicio()
        w = x[0]
        k = 1
        while c > 1:
            y = filas.removeInicio()
            if len(y) == 0:
                juvenal = False
                break
            else:
                z = y[0]
                if w == z:
                    y = y[1:]
                    filas.inserirFim(y)
                    c -= 1
                    k += 1
                else:
                    del y[0]
                    y.append(z)
                    filas.inserirFim(y)
                    c -= 1
                    k += 1
        if not juvenal:
            break
        del x[0]
        x.append(w)
        cartasMesa.inserirFim(x)
        rodadas -= 1
    if juvenal:
        arqSaida.write("0\n")
    else:
        arqSaida.write(str(k)+"\n")
