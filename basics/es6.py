# funzione id

i = 0
print(id(i))

i += 1
print(id(i))

stringa1 = 'ciao'
print(id(stringa1))
stringa1 += 'ciao'
print(id(stringa1))

tupla1 = (1, 2)
print(id(tupla1))
tupla1 += (3, 4)
print(id(tupla1))

# mutable

lista1 = [1, 2]
print(id(lista1))
lista1.append(3)
print(id(lista1))

