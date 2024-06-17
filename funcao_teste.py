def saque(*, valor_saque, excedeu_limite):
    if valor_saque > excedeu_limite :
        print("Saque Realizado com sucesso ")
    elif valor_saque < excedeu_limite:
        print("execdeu o limite")
    else:
        print("fechar programa")
saque(valor_saque=300, excedeu_limite=150)
