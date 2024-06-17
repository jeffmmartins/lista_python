 
menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar conta 
    [nu] Novo usuario
    [q] Sair 
    => """


AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = 

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

def novo_usuario(usuarios):
    cpf = int(input("difgite seu cpf:"))
    usuario = filtro_usuario(cpf, usuarios)
     
    if usuario:
          print("\nUsuario já cadastrado")
          return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereco (logradouro, nro - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cadastrado com sucesso")

def filtro_usuario(cpf,usuarios)
     filtro_novos_usuarios = [usuario for usuario in usuarios  if usuarios["cpf"] == cpf ]
     return filtro_novos_usuarios[0] if filtro_novos_usuarios else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = int(input("Digite o cpf: "))
     usuario = filtro_usuario(cpf, usuarios)
     
     if usuarios: 
          print("\nConta criada")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuario}
     

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
    elif opcao == "nu":
         novo_usuario(usuarios)
    elif opcao == "nc":
         criar_conta(AGENCIA, numero_conta, usuarios)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")