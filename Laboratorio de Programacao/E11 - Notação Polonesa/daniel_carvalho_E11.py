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
operandos = Pilha()
while True:
    expressao = (arqEntrada.readline()).split()
    if not expressao:
        break
    for i in range(len(expressao)-1,-1,-1):
        if (expressao[i] == '*'):
            a = int(operandos.removeFim())
            b = int(operandos.removeFim())
            r = int(a)*int(b)
            operandos.inserirFim(r)
        elif (expressao[i] == '+'):
            a = int(operandos.removeFim())
            b = int(operandos.removeFim())
            r = int(a)+int(b)
            operandos.inserirFim(r)
        elif (expressao[i] == '-'):
            a = int(operandos.removeFim())
            b = int(operandos.removeFim())
            r = int(a)-int(b)
            operandos.inserirFim(r)
        elif (expressao[i] == '/'):
            a = int(operandos.removeFim())
            b = int(operandos.removeFim())
            r = int(a)//int(b)
            operandos.inserirFim(r)
        else:
            operandos.inserirFim(expressao[i])
    resultado = operandos.removeFim()
    arqSaida.write(str(resultado)+"\n")
arqEntrada.close()
arqSaida.close()    
