def saque(*, excedeu_limite):
    saque  = float(input("digite um valor: "))
    if saque < excedeu_limite :
        print("Saque Realizado com sucesso ")
    else:
        print("voce excedeu o limite")
    
saque(excedeu_limite=400)

