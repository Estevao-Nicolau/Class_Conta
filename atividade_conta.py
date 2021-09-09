# Programação Orientada a Objetos
# AC02 ADS-EaD - Implementação de classes
#
# Email Impacta: estevao.brito@aluno.faculdadeimpacta.com.br


class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo_inicial
        self.__ativa = False
        self.__operacoes = [('saldo inicial', saldo_inicial)]


    @property
    def titular(self):
        return self.__titular


    @property
    def agencia(self):
        return self.__agencia


    @property
    def numero(self):
        return self.__numero

    @property
    def ativa(self):
        return self.__ativa


    @property
    def saldo(self):
        return self.__saldo


    @ativa.setter
    def ativa(self, situacao):
        if isinstance(situacao, bool):
            self.__ativa = situacao
        return


    def depositar(self, valor):
        if self.__ativa == True and valor > 0:
            self.__saldo += valor
            self.__operacoes.append(('deposito', valor))
        return


    def sacar(self, valor):
        if self.__ativa == True and self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            self.__operacoes.append(('saque', valor))
        return


    def transferir(self, conta_destino, valor):
        if self.__ativa == True and conta_destino.ativa == True:
            if valor > 0 and valor <= self.__saldo:
                self.sacar(valor)
                conta_destino.depositar(valor)
                self.__operacoes.append(('transferencia', valor))
        return


    def tirar_extrato(self):
        return self.__operacoes
