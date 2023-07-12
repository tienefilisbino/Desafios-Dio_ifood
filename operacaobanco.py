menu = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
=> '''
saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == 'd':
        deposito = int(input("Qual valor deseja deposita : "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + f'Deposito: R$ {deposito:.2f}\n'
        else:
            print("Falha: Valor inválido")
    elif opcao == 's':
        saque = int(input("Qual valor deseja sacar : "))
        if saque > 500:
            print("valor acima do limite de R$ 500,00")
        elif saque <= 0:
            print("Valor inválido. Inseririr valor válido")
        elif LIMITE_SAQUES > 0:
            print("exedeu o valor de saque diários.")
        elif saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo = saldo - saque
            extrato = extrato + f'saque: R$ {saque:.2f}\n'
            LIMITE_SAQUES = LIMITE_SAQUES - 1
    
    elif opcao == 'e':
        print('********** Extrato **********')
        if not extrato:
            print("Não houve operação")
            print(f"O saldo é {saldo}")
            print('************************')
        else:
            print(extrato)
            print(f"O saldo é {saldo}")
            print('**************************')
    elif opcao == 'q':
        break
    else:
        print("digite um valor válido.")
    
