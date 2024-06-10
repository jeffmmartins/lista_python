pessoa = {"nome" : "Jefferson", "idade" : 35}
print(pessoa)

pessoa = dict(nome="Jake", idade= 18)

# acrescentando uma chave e  valor no dicionario
pessoa["telefone"] = "3333-3333"
print(pessoa)

#acessando os dados 
informacoes = {"nome": "Vera", "idade": 35}
print(informacoes["nome"])

#dicionarios aninhados 
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
 "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
 "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
 "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
 }
print(contatos["giovanna@gmail.com"]["telefone"])

for chave, valor in contatos.items():
    print(chave, valor)