"""
Script per trovare il numero più grande di una lista
"""

lista = [5, 23, 6, 262, 78, 2, 54]

massimo = max(lista)

print(f"Somma degl elementi della lista: {massimo}")

# alternativa usando loop

massimo = lista[0]
for numero in lista:
    if numero > massimo:
        massimo = numero



print(f"Somma degl elementi della lista (alternativa): {massimo}")


