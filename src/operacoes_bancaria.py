depositos:list = []
saques:list = []
extrato:list = []
LIMITE_SAQUE:int = 3
VALOR_SAQUE:float = 500

def sacar():
    """
    Realiza a operação de saque.

    Solicita ao usuário o valor do saque e realiza as seguintes validações:
    - O valor deve ser positivo.
    - O número de saques não pode ultrapassar o limite diário (LIMITE_SAQUE).
    - O valor do saque não pode exceder o valor máximo permitido por saque (VALOR_SAQUE).
    - O saldo deve ser suficiente para o saque.

    Se todas as condições forem atendidas, registra o saque e atualiza o extrato.
    """
    saldo = sum(depositos) - sum(saques)
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Valor inválido para saque.")
        return
    if len(saques) >= LIMITE_SAQUE:
        print("Limite de saques atingido.")
        return
    if valor > VALOR_SAQUE:
        print("Valor do saque excede o limite permitido.")
        return 
    if saldo < valor:
        print("Saldo insuficiente para realizar o saque.")
        return 
    saques.append(valor)
    extrato.append(f"Saque: {valor}")
    print("Saque realizado com sucesso.")
    

def depositar():
    """
    Realiza a operação de depósito.

    Solicita ao usuário o valor do depósito. Se o valor for positivo,
    adiciona à lista de depósitos, registra no extrato e exibe mensagem de sucesso.
    Caso contrário, informa que o valor é inválido.
    """
    valor = float(input("Digite o valor do depósito: "))
    if valor <= 0:
        print("Valor inválido para depósito.")
        return
    depositos.append(valor)
    extrato.append(f"Depósito: {valor}")
    print("Depósito realizado com sucesso.")


def visualizar_extrato():
    """
    Exibe o extrato das transações.

    Mostra todas as transações registradas no extrato, o total de depósitos,
    o total de saques e o saldo atual. Caso não haja transações, informa que
    nenhuma transação foi realizada.
    """
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print("Extrato:")
        for transacao in extrato:
            print(transacao)
    print(f"Total de depósitos: R$ {sum(depositos):.2f}")
    print(f"Total de saques: R$ {sum(saques):.2f}")
    print(f"Saldo atual: R$ {(sum(depositos) - sum(saques)):.2f}")


menu = """
Bem-vindo ao sistema bancário!

-- Menu de operações ---
1. Sacar
2. Depositar
3. Visualizar extrato
4. Sair

Escolha uma opção:
"""

while True:
    opcao = input(menu)
    
    if opcao == '1':
        sacar()
    elif opcao == '2':
        depositar()
    elif opcao == '3':
        visualizar_extrato()
    elif opcao == '4':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
