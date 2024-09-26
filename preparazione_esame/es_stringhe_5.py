"""
Script per cercare all'interno di una stringa
"""

stringa = input("Dammi una stringa: ")
stringa_ricercata = input("Cosa vuoi cercare? ")

# con la keyword `in` possiamo chiedere a python di cercare all'interno di una lista o di una stringa

if stringa_ricercata in stringa:
    print(f"{stringa_ricercata} è presente nella stringa {stringa}")
else:
    print(f"{stringa_ricercata} non è presente nella stringa {stringa}")