 
menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar conta 
    [nu] Novo usuario
    [q] Sair 
    => """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor, saldo, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato 

def sacar(*, valor, saldo, limite, numero_saques,limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.") 

def mostrar_extrato(saldo, /, *, extrato ):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo, extrato
     
while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)
            
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

    
    elif opcao == "e":
        saldo, extrato = mostrar_extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")