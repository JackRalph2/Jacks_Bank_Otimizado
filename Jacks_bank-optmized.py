def menu():
    menu = """
===========JACK'S BANK============
----------Seja Bem-Vindo!---------

===>Selecione a opção desejada<===
    (s) Sacar
    (d) Depositar
    (e) Extrato
    (1) Criar Usuário
    (2) Criar Conta
    (3) Listar contas ativas
    (q) Sair

==================================
"""
    
def depositar(saldo, valor, extrato, /):
    while True:
            try:
                valor = float(input("Informe o valor a ser depositado: R$"))
            except ValueError as str:
                print("\nOperação inválida! Utilize apenas números.\n")
            else:
                break
            if valor > 0:
                saldo += valor
                extrato += f"\nDepósito no valor de R$ {valor:.2f}"
            print("\nDepósito realizado com sucesso!")

    else: print("Valor informado é inválido")
    
    return saldo, extrato
    
def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    
    print("Saque")
    while True:
            try:
                saque = float(input("Digite o valor desejado: R$"))
            except ValueError as str:
                print("\nOperação inválida! Utilize apenas números.\n")
            else:
                break
    excedeu_saldo = saque > saldo
    limite_excedido = saque > limite
    limite_diario = numero_saques >= limite_saques

    if excedeu_saldo:
            print("\nOperação não realizada. Saldo insuficiente :/")
    elif limite_excedido:
            print("\nLimite por saque (R$500) excedido")
    elif limite_diario:
            print("\nLimite diário de saques excedido. Volte amanhã ;)")
        
    else:
            print("\nSaque no valor de R$", saque, "realizado com sucesso!")
            numero_saques += 1
            saldo -= saque
            extrato += f"\nSaque no valor de R$ {saque:.2f}"
    
def exibir_extrato(saldo, /, *, extrato):
    print("===========JACK'S BANK============")
    print("   \n==========EXTRATO==========    ")
    print("Não houve movimentação" if not extrato else extrato)
    print(f"\nSaldo R${saldo:.2f}")
    print("\n   ===========================   ")
    
def criar_usuario(usuarios):
     cpf = input("Informe seu CPF (somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Erro: Usúario já existente!")
          return
     
     nome = input("Informe seu nome completo: ")
     data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe seu endereço completo: ")

     usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

     print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuario: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\nConta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("\nUsuário não encontrado! Retornando ao menu principal")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C:\t\t{conta["usuario"]['nome']}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("="* 100)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    mensagem_final = "\nMuito obrigado por utilizar o Jack' Bank!"

    while True:
        opcao = menu()

        if opcao == "d":
            valor - float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)



        elif opcao == "e":
             exibir_extrato(saldo, extrato=extrato)
        

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
              saldo=saldo,
              valor=valor,
              extrato=extrato,
              limite=limite,
              numero_saques=numero_saques,
              limite_saques=LIMITE_SAQUES,
         )
            
        elif opcao == "1":
             criar_usuario(usuarios)

        elif opcao == "2":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)

        elif opcao == "3":
             listar_contas(contas)
        
        elif opcao == "q":
            print(mensagem_final)
        break

    else:
        print("Opção inválida. Tente novamente.")
    
main()