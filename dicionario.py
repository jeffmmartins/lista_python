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

#metodos
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
 "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
 "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
 "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
 }
contatos.clear()
contatos  # {}

#copy()
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
 }
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
contatos["guilherme@gmail.com"]  # {"nome": "Guilherme", "telefone": "3333
2221"}
copia["guilherme@gmail.com"]  # {"nome": "Gui"}

#fromkeys()
dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"} 

#GET
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
 }
contatos["chave"]  # KeyError
contatos.get("chave")  # None
contatos.get("chave", {})  # {}
contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

#keys
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
 }
contatos.keys() 

#pop
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
 }
contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '33332221'}
contatos.pop("guilherme@gmail.com", {})  # {}

#POPITEM
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
 }
contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos.popitem()  # KeyErro

#SETDEFAULT
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("nome", "Giovanna")  # "Guilherme"
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("idade", 28)  # 28 caso nao exista a chave ele adiciona a chave e o valor
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}


#UPDATE
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
 }
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}}
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "33228181"}})
contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

#VALUES
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
 "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
 "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
 "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
 }
contatos.values()  # dict_values([{'nome': 'Guilherme', 'telefone': '33332221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])

#IN
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
 "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
 "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
 "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
 }
 "guilherme@gmail.com" in contatos  # True
 "megui@gmail.com"incontatos  # False
 "idade" in contatos["guilherme@gmail.com"]  # False
 "telefone" in contatos["giovanna@gmail.com"]  # True

#DEL
contatos = {
 "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
 "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
 "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
 "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
 }
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]
contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2

