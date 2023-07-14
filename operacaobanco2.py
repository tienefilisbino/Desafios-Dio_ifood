

def menu():
    menu = '''
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] nova conta
    [lc] listar conta
    [nu] novo usuário
    [q] Sair
    => '''
    return input(menu)

def depositar(saldo,deposito,extrato,/):
    if deposito > 0:
        saldo =  saldo + deposito
        extrato = f'Deposito: R$ {deposito:.2f}\n'
    else:
        print("Falha: Valor inválido")
    return saldo,extrato

def sacar(*,saldo,saque,extrato,limite_saques):
    if saque > 500:
        print("valor acima do limite de R$ 500,00")
    elif saque <= 0:
        print("Valor inválido. Inseririr valor válido")
    elif limite_saques == 0:
        print("exedeu o valor de saque diários.")
    elif saque > saldo:
        print("Saldo insuficiente.")
    else:
        saldo = saldo - saque
        extrato = extrato + f'saque: R$ {saque:.2f}\n'
        limite_saques = limite_saques - 1
    return saldo,extrato,limite_saques

def exibir_extrato(saldo,/,*,extrato):
    print('********** Extrato **********')
    if not extrato:
        print("Não houve operação")
        print(f"O saldo é {saldo}")
        print('************************')
    else:
        print(extrato)
        print(f"O saldo é {saldo}")
        print('**************************')

def criar_usuario(usuarios):
    cpf = input('Informe o número do cpf: ')
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print('Usuário existente')
        return
    nome=input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa):')
    endereco = input('Informe o endereço (rua - bairro- cidade): ')
    usuarios.append({'nome':nome,'data_nascimento': data_nascimento,'cpf':cpf,'endereco':endereco})
    print('Usuário criado!')

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input('Informe o número de cpf: ')
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print('Conta criada!')
        return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}
    
    print('Usuario não encontrado!')

def listar_conta(contas):
    for conta in contas:
        linha = f'''
            Agencia = \t{conta['agencia']}
            conta = \t\t{conta['numero_conta']}
            usuario = \t{conta['usuario']['nome']}
            '''
        print(linha)

def main():
    AGENCIA='001'
    saldo = 0
    limite = 500
    extrato = ""
    usuarios=[]
    contas=[]
    LIMITE_SAQUES = 3
    while True:
        opcao = menu()
        if opcao == 'd':
            deposito = int(input("Qual valor deseja deposita : "))
            saldo,extrato = depositar(saldo,deposito,extrato)

        elif opcao == 's':
            saque = int(input("Qual valor deseja sacar : "))
            saldo,extrato,limite_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite_saques=LIMITE_SAQUES,
            )
            LIMITE_SAQUES=limite_saques
       
    
        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)
        elif opcao =='nu':
            criar_usuario(usuarios)
        elif opcao =='nc':
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_conta(contas)

        
        elif opcao == 'q':
            break
        else:
            print("digite um valor válido.")
main()
    
