# tupla
# immutable

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (1, 'a', True)


for elem in tupla1:
    print(elem)

print(tupla2.index(True))
print(tupla1.count(3))

lista1 = ['a', 'b', 'c']
tupla3 = (1, 2, 3, lista1)
print(tupla3)

lista1.append('d')
print(lista1)
print(tupla3)

# non posso aggiungere elementi alla tupla, ma posso creare una nuova tupla con i nuovi elementi
tupla4 = tupla1 + tupla2
print(tupla4)
