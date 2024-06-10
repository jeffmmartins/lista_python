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

#Argumentos nomeados 
def salvar_carro(marca, modelo, ano, placa):
 # salva carro no banco de dados...
 print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
 salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
 salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
 salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) #passando como dicionario
 # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234]

 #Args e Kwargs
def exibir_poema(data_extenso, *args, **kwargs):
 texto = "\n".join(args)
 meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in
 kwargs.items()])
 mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
 print(mensagem)
 exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim 
Peters", ano=1999)]

#Positional Only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
 print(modelo, ano, placa, marca, motor, combustivel)
 criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
combustivel="Gasolina")  # válido
 criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina")  # inválido

#Keword Only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
 print(modelo, ano, placa, marca, motor, combustivel)
 criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina")  # válido
 criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
combustivel="Gasolina")  # inválido

#Objetos de Primeira Classe
def somar(a, b):
 return a + b

 def exibir_resultado(a, b, funcao):
 resultado = funcao(a, b)
 print(f"O resultado da operação {a} + {b} = {resultado}")
 exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

 #escopo Global e local
 salario = 2000 

 def salario_bonus(bonus):
 global salario
 salario += bonus
 return salario
 salario_bonus(500)  # 2500


