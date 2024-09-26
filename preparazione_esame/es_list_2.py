"""
Script per sommare tutti gli elementi di una lista
"""

lista = [1, 2, 3, 4, 5]

total = sum(lista)

print(f"Somma degl elementi della lista: {total}")

# alternativa usando loop

total = 0
for numero in lista:
    total += numero

print(f"Somma degl elementi della lista (alternativa): {total}")