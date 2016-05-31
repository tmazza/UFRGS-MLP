#!/usr/bin/python

import thread
import time
import random

produtosDisponiveis = [
    ["MAC book Air",2400.00],
    ["Eeee PC",654.00],
    ["Acer Aspire One",710.00],
    ["DVD virgem",0.75],
    ["CD virgem",0.35],
    ["Flashdrive 4GB",19.00],
];

class Produto:
    def __init__(self,cod,descricao,custo,lucro):
        self.cod = cod
        self.descricao = descricao
        self.custo = custo
        self.lucro = lucro
        self.qtdEstoque = random.randrange(0, 100)
        self.qtdVendida = 0

    def __str__(self):
        return "%d: %s | Custo R$%d,00" % (self.cod,self.descricao,self.custo)

    def valorFinal(self):
        return self.custo * self.lucro

    def valorEmEstoque(self):
        return self.valorFinal() * self.qtdEstoque()

class Estoque:
    def __init__(self):
        self.produtos = []; # Produto.cod: qtd
        self.cod = 0;

    def addProdutos(self):
        qtd = random.randrange(2, 10) # Qtd de produtos que sera adicionada
        for i in range(0,qtd):
            indice = random.randrange(0, len(produtosDisponiveis)) # Soteia produto que ser adicionado
            sorteado = produtosDisponiveis[indice]
            lucro = 1 + (random.randrange(2, 8) / 10)
            p = Produto(self.cod,sorteado[0],sorteado[1],lucro)
            self.produtos.append(p)
            self.cod += 1
            print "Incluido no estoque: %s" % (p)

    def getProdutoComprado(self):
        if(len(self.produtos) > 0):
            return self.produtos.pop()
        else: return False


estoque = Estoque()

def alimentaEstoque():
    while 1:
        estoque.addProdutos()
        time.sleep(7)

def realizaCompra( cliente ):
    while 1:
        time.sleep(3)
        comprado = estoque.getProdutoComprado()
        if comprado:
            print "\o/ %s comprou o produto %s" % (cliente, comprado)
        else:
            print ":(  %s nao encontrou nada no estoque"  % (cliente)

try:
   # Fornecedor(es)
   thread.start_new_thread( alimentaEstoque, () )
   # Clientes
   thread.start_new_thread( realizaCompra, ( "Cliente 1", ) )
   thread.start_new_thread( realizaCompra, ( "Cliente 2", ) )
   thread.start_new_thread( realizaCompra, ( "Cliente 3", ) )
except:
   print "Erro ao criar thread"

while 1: # para manter terminal ativo e ver out das threads
   pass
