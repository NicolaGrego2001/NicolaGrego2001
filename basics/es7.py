# set

set1 = {1, 2, 3, 4}
print(set1)
print(id(set1))

set1.add(5)
print(set1)
print(id(set1))

set1.add(3)
print(set1)
print(id(set1))

# lista con elementi ripetuti


lista = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

print(lista)

set1 = set(lista)
print(set1)

set1 = set()
for elemento in lista:
    print(elemento)
    set1.add(elemento)
print(set1)

