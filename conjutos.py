# exclui os elementos repetidos , lembrando que não deve confiar na ordem 

numeros = set([1,2,3,1,3,4])
print(numeros) 

letras = set("abacaxi")
print(letras)

numeros = {1,2.3,4}
numeros =list(numeros)

print(numeros[0])

carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)

# Metodos da classe set

conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))  # {2, 3}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.difference(conjunto_b))  # {1}
print(conjunto_b.difference(conjunto_a))  # {4}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.symmetric_difference(conjunto_b))  # {1, 4}

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a))  # False

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a))  # True

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop()  # 0
numeros.pop()  # 1
numeros  # {2, 3, 4, 5, 6, 7, 8, 9

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0)  # 0
numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros)  # 10

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
1 in numeros  # True
10 in numeros  # False