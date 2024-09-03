# misc

lista1 = ['a', 'b', 'c']

for elemento in lista1:
    print(elemento)

for index, elemento in enumerate(lista1):
    print(f'Indice: {index}, Elemento: {elemento}')

lista2 = [1, 2, 3]
for lettera, numero in zip(lista1, lista2):
    print(f'Lettera: {lettera}, Numero: {numero}')