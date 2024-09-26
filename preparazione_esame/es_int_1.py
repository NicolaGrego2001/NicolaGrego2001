"""
Script per controllare se un intero è positivo o negativo
"""

# la funzione input ritorna una stringa. Dobbiamo fare il casting per avere un intero
numero = int(input(f"Dammi un numero: "))

if numero > 0:
    print(f"{numero} è un numero positivo")
elif numero < 0:
    print(f"{numero} è un numero negativo")
else:
    print(f"{numero} è zero")

