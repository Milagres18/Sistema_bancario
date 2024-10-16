class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def visualizar_extrato(self):
        print(f"\nExtrato de {self.titular}:")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


def menu():
    print("===== Sistema Bancário =====")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")

def main():
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(titular=nome)

    while True:
        menu()
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor a depositar: R$"))
                conta.depositar(valor)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor a sacar: R$"))
                conta.sacar(valor)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        elif opcao == '3':
            conta.visualizar_extrato()
        elif opcao == '4':
            print("Encerrando o sistema. Obrigado por usar nossos serviços!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()
