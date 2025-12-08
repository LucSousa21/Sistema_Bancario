import os
data_base = {} 
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return
        self.saldo += valor
        self.extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def ver_extrato(self):
        print("\n=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação.")
        for mov in self.extrato:
            print(mov)
        print(f"Saldo atual: R$ {self.saldo:.2f}")




while True:


    print("Bem-vindo(a) ao Banco do Lucas!")
    print("*******************************")
    print("\ Menu de Opções /")
    print("1 - Depositar Dinheiro")
    print("2 - Sacar Dinheiro")
    print("3 - Ver Saldo")
    print("4 - Ver Extrato")
    print("5 - Criar Conta")


    dicionario_menu = {
        1: "Depositar Dinheiro",
        2: "Sacar Dinheiro",
        3: "Ver Saldo",
        4: "Ver Extrato",
        5: "Criar Conta"
    }
    menu = int(input("Escolha uma opção: "))

    # Limpa a tela para melhor visualização em varios sistemas operacionais
    os.system('cls' if os.name == 'nt' else 'clear')


    print(f"Opção escolhida: {dicionario_menu[menu]}")

    match menu:
        case 1: # Depositar Dinheiro
            titular = input("Digite o nome do titular da conta: ").strip().lower()
            if titular not in data_base:
                print("Conta não encontrada. Por favor, crie uma conta primeiro.")
                continue
            else:
                conta = data_base[titular]
                conta.depositar(float(input("Digite o valor a ser depositado: R$ ")))
            
        case 2: # Sacar Dinheiro
            titular = input("Digite o nome do titular da conta: ").strip().lower()
            if titular not in data_base:
                print("Conta não encontrada. Por favor, crie uma conta primeiro.")
                continue
            else:
                conta = data_base[titular]
                conta.sacar(float(input("Digite o valor a ser sacado: R$ ")))
        
        case 3: # Ver Saldo
            titular = input("Digite o nome do titular da conta: ").strip().lower()
            if titular not in data_base:
                print("Conta não encontrada. Por favor, crie uma conta primeiro.")
                continue
            else:
                conta = data_base[titular]
                conta.ver_saldo()
        
        case 4: # Ver Extrato
            titular = input("Digite o nome do titular da conta: ").strip().lower()
            if titular not in data_base:
                print("Conta não encontrada. Por favor, crie uma conta primeiro.")
                continue
            else:
                conta = data_base[titular]
                conta.ver_extrato()
        
        case 5: # Criar Conta
            titular = input("Digite o nome do titular da conta: ").strip().lower()
            if titular in data_base:
                    print("Conta já existente para este titular.")
                    
            else:
                
                nova_conta = ContaBancaria(titular=titular)
                data_base[titular] = nova_conta
                
                print(f"Conta criada com sucesso para {titular}!")
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")

