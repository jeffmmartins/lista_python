lista = [1,2,3,4]

lista.clear()
print(lista)

numeros = [1,3,4,5]
numeros.copy()
print(numeros)


#extend
linguagens = ["python", "js", "c"]
linguagens.extend(["java", "kotlin"])
print(linguagens)

#index
linguagen = ["python", "js", "c", "java", "csharp"]
print(linguagen.index("java"))
print(linguagen.index("python"))  

#pop
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop())  # csharp
print(linguagens.pop()) # java
print(linguagens.pop())  # c
print(linguagens.pop(0))

#remove
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens) 

#reverse
linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.reverse()
print(linguagens) 

#sort
linguagen = ["python", "js", "c", "java", "csharp"]
print(linguagen.sort())  # ["c", "csharp", "java", "js", "python"]
linguagen = ["python", "js", "c", "java", "csharp"]
print(linguagen.sort(reverse=True))  # ["python", "js", "java", "csharp", "c"]
linguagen = ["python", "js", "c", "java", "csharp"]
print(linguagen.sort(key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
linguagen = ["python", "js", "c", "java", "csharp"]
print(linguagen.sort(key=lambda x: len(x), reverse=True))

#len
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))

#sorted
linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x))) # ["c", "js", "java", "python", 

print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ["python", "csharp", "java", "js", "c"]

