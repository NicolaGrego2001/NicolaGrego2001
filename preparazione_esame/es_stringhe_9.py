"""
Script per controllare se una stringa è palindroma
"""

stringa = input("Dammi una stringa: ")

# con splicing
stringa_invertita = stringa[::-1]

# controllo
if stringa == stringa_invertita:
    print(f"{stringa} è palindroma")
else:
    print(f"{stringa} non è palindroma")

