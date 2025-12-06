import os


def depositar_dinheiro(valor):
    saldo += valor
    return saldo

def sacar_dinheiro(valor):
    saldo -= valor
    return saldo


#def ver_extrato():


def ver_saldo():
    saldo = 0
    return saldo


#def criar_conta():




print("Bem-vindo(a) ao Banco do Lucas!")
print("*******************************")
print("\ Menu de Opções /")
print("1 - Depositar Dinheiro")
print("2 - Sacar Dinheiro")
print("3 - Ver Extrato")
print("4 - Ver Saldo")
print("5 - Criar Conta")


dicionario_menu = {
    1: "Depositar Dinheiro",
    2: "Sacar Dinheiro",
    3: "Ver Extrato",
    4: "Ver Saldo",
    5: "Criar Conta"
}
menu = int(input("Escolha uma opção: "))

os.system('cls')

print(f"Opção escolhida: {dicionario_menu[menu]}")

match menu:
    case 1:
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        depositar_dinheiro(valor_deposito)
    case 2:
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        sacar_dinheiro(valor_saque)
    case 3:
        pass
    case 4:
        saldo_atual = ver_saldo()
        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")
    case 5:
        pass
    case _:
        print("Opção inválida. Por favor, escolha uma opção válida.")

