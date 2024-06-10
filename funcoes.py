def exibir_mensagem(nome):
    print(f"meu nome é {nome}")

exibir_mensagem("Jefferson")

def calcular_total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10, 20, 30]))
print(antecessor_sucessor(10))