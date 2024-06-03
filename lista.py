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

#compreensão de lista 

numeros = [1, 23, 45, 78, 89, 4, 8]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)

numeros = [1, 23, 45, 78, 89, 4, 8]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

numeros = [1, 23, 45, 78, 89, 4, 8]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
