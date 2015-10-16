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
                return "Valor nao encontrado!"
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

class Pilha(ListaEncadeada):
    def removeFim(self):
        if self.isEmpty():
            return "Lista vazia!"
        else:
            valorUltimoNode = self._fim.getData()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
                #print(valorUltimoNode)
            else:
                temp = self._fim.getprevNode()
                self._fim.setprevNode(None)
                temp.setNextNode(None)
                self._fim = temp
                #print(valorUltimoNode)
    
                
print("##################\nLista:")
lista = ListaEncadeada()
lista.inserirFim(10)
lista.inserirFim(20)
lista.imprimir()
print("===========\nRemovendo o elemento 10...\n===========")
lista.remover(10)
lista.imprimir()
print("===========\nEsvaziando...\n===========")
lista.esvaziar()
lista.imprimir()
print("\n##################")
print("Fila:")
fila = Fila()
fila.inserirFim(1)
fila.inserirFim(3)
fila.inserirFim(5)
fila.imprimir()
print("===========\nAtendendo o primeiro da fila\n===========")
fila.removeInicio()
fila.imprimir()
print("\n##################")
print("Pilha")
pilha = Pilha()
pilha.inserirFim(10)
pilha.inserirFim(11)
pilha.inserirFim(12)
pilha.imprimir()
print("===========\nRemovendo o ultimo elemento adicionado...\n===========")
pilha.removeFim()
pilha.imprimir()