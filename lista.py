matriz = [
    ["b", 11,4],
    ["c", 34,3],
    [23, 11,"f"]
]

# primeiro valor indica a linha e segundo valor indica coluna
print(matriz[1][1])

lista = ["p","y","t","h","o","n"]
print(lista[0:3:2]) # inicio, final , step
print(lista[2:]) 
print(lista[:2]) 

#percorrendo lista 
carros = ["gol", "polo", "jeta"]

for carro in carros:
    print(f"lista de carros: {carro}")

#enumerate
carros = ["gol", "polo", "jeta"]

for indice,carro in enumerate(carros):
    print(f"{indice + 1} = {carro}")