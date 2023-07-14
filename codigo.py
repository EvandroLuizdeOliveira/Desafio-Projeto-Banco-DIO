menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor a ser depositado: R$"))
        if deposito > 0:
            saldo += deposito
            extrato = f"Depósito R${deposito:.2F}\n{extrato}"
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nValor inválido!")

    elif opcao == "2":
        saque = float(input("Digite o valor a ser sacado: R$"))
        if numero_saque == LIMITE_SAQUES:
            print("\nLimite de saque diário atingido!")
        elif saque > saldo:
            print("\nSaldo insuficiente!")
        elif saque > limite:
            print("\nValor supera o limite de saque diário de R$500!")
        elif saque <= limite and numero_saque <=3 and saldo >= saque:
            saldo -= saque
            numero_saque += 1
            extrato = f"Saque R${saque:.2F}\n{extrato}"
            print("\nSaque realizado com sucesso!")
        else:
            print("\nErro desconhecido!")

    elif opcao == "3":
        print()
        print("Extrato".center(40, "#"))
        if not extrato:
            print("\nNão foram realizadas movimentações.")
        elif extrato:
            print(f"{extrato}",end="")
        print(f"\nSaldo: R${saldo:.2F}")
        print(f"{40 * '#'}")
    
    elif opcao == "4":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
