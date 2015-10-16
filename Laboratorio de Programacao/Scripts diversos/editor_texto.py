####################################################
# Exemplo de entrada:                              #
#  > adicionar abacaxi e bom - Escreve		   #
#  > apagar 2 - Apaga a quantidade determinada	   #
#  > desfazer - Desfaz as alteracoes		   #
#  > refazer - Refaz o ultimo passo		   #
#  > negrito, italico - Escreve o formato	   #
#						   #
#						   #
####################################################

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
            return valorPrimeiroNode

class Pilha(ListaEncadeada):
    def removeFim(self):
        if self.isEmpty():
            return
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

arqEntrada = open(sys.argv[1],"r")
arqSaida = open(sys.argv[2],"w")
refazer = Pilha()
texto = Pilha()
formatos = Pilha()
s = " "
frase = ""
while (True):
    linha = (arqEntrada.readline()).split()
    tamanho = len(linha)
    c = 0
    if (tamanho == 0):
        break
    comando = linha[0]
    if (comando == "adicionar"):
        refazer.esvaziar()
        if texto.isEmpty():
            x = linha[1:]
            texto.inserirFim(x)
        else:
            x = texto.removeFim() + linha[1:]
            texto.inserirFim(x)
    elif (linha[0] == "italico"):
        refazer.esvaziar()
        if formatos.isEmpty():
            formatos.inserirFim("italico")
        else:
            x = formatos.removeFim() + " italico"
            formatos.inserirFim(x)
    elif (linha[0] == "negrito"):
        refazer.esvaziar()
        if formatos.isEmpty():
            formatos.inserirFim("negrito")
        else:
            x = formatos.removeFim() + " negrito"
            formatos.inserirFim(x)
    elif (linha[0] == "apagar"):
        passos = int(linha[1])
        c = texto.removeFim()
        d = c[:-passos]
        texto.inserirFim(c)
        texto.inserirFim(d)
    elif (linha[0] == "desfazer"):
        c = texto.removeFim()
        refazer.inserirFim(c)
    elif (linha[0] == "refazer"):
        if refazer.isEmpty():
            pass
        else:
            elemento = refazer.removeFim()
            texto.inserirFim(elemento)

#while (not texto.isEmpty() or not formatos.isEmpty()):
var = texto.removeFim()
for i in range(len(var)):
    frase = frase + "%s " % var[i]
arqSaida.write(frase + " | " + str(formatos.removeFim()))
