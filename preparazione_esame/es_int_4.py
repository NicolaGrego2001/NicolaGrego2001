"""
Script per trovare il numero più grande tra due numeri in input
"""
numero_1 = int(input(f"Dammi il primo numero: "))
numero_2 = int(input(f"Dammi il secondo numero: "))

if numero_1 > numero_2:
    print(f"{numero_1} è il numero più grande")
else:
    print(f"{numero_2} è il numero più grande")
