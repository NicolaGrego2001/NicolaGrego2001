# misc

lista1 = ['a', 'b', 'c']

for elemento in lista1:
    print(elemento)

for index, elemento in enumerate(lista1):
    print(f'Indice: {index}, Elemento: {elemento}')

lista2 = [1, 2, 3]
for lettera1, numero1, lettera2, numero2 in zip(lista1, lista2, lista1, lista2):
    print(f'Lettera: {id(lista1)}, Numero: {numero1} || Lettera: {lettera2}, Numero: {numero2}')