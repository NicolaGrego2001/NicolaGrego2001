"""
Script per stampare la tabellina della moltiplicazione di numero
"""

numero = int(input(f"Dammi un numero: "))

for i in range(1, 11):  # la tabellina da 1 a 10 (ricordatevi che il range si interrompe prima di arrivare al secondo numero
    print(f"{numero} x {i} = {numero * i}")

