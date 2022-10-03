class ContaCorrente:
    def __init__ (self, nomecorren, num, saldo=0):
      self.nomecorren = str(nomecorren)
      self.num = int(num)
      self.saldo = saldo

    def alterarNome(self,nvnome):
      op = "Y"
      opção = input("Deseja mudar o nome? Digite Y p/sim e N p/não:")
      if opção == op:
        nvnome = input("Escreva o novo nome: ")
        self.nomecorren = nvnome
      return self.nomecorren
      ContaCorrente.exibir()
  
    def deposito(self,valordep):
      r = "Y"
      resposta = input("Deseja fazer um depósito? Digite Y p/sim e N p/não:")
      if resposta == r:
        valordep = input("Insira o valor do depósito: ")
        self.saldo += valordep
      return self.saldo
      ContaCorrente.exibir()

    def saque(self,valorsaq):
      r = "Y"
      resposta = input("Deseja fazer um saque? Digite Y p/sim e N p/não:")
      if resposta == r:
        valorsaq = input("Insira o valor do saque: ")
        self.saldo -= valorsaq
      return self.saldo
      ContaCorrente.exibir()

    def exibir(self):
      print ("Nome: {}".format(self.nomecorren))
      print ("Número da Conta: {}".format(self.num))
      print ("Seu saldo atual é: R${}".format(self.saldo))

Correntista = ContaCorrente ("Juliana Silva", 1068, "10000")
Correntista.exibir()
print(input(" "))

import os
os.system('clear') or None

print ("----------------------------")
Correntista.alterarNome("Y")
print ("----------------------------")
print(input(" "))

import os
os.system('clear') or None

print ("----------------------------")
print ("---PROCESSANDO O DEPÓSITO---")
print ("----------------------------")
print(input(" "))

import os
os.system('clear') or None

print ("-----------------------------")
Correntista.deposito(0)
print ("-----------------------------")
Correntista.exibir()
print(input(" "))

import os
os.system('clear') or None

print ("-----------------------------")
print ("-----PROCESSANDO O SAQUE-----")
print ("-----------------------------")
print(input(" "))

import os
os.system('clear') or None

print ("-----------------------------")
Correntista.saque(0)
print ("-----------------------------")
Correntista.exibir()
