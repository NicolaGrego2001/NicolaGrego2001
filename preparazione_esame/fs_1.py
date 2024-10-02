"""
Scrivere uno script per estrarre una lista di numeri pari a
partire da una lista di numeri random
"""

import random

lista_input = [random.randint(1, 100) for _ in range(1024)]

lista_numeri_pari = []
for numero in lista_input:
    if numero % 2 == 0:
        # è pari
        lista_numeri_pari.append(numero)
    else:
        continue

print(lista_numeri_pari)
