"""
Script per controllare se una stringa inizia con una lettera
"""

stringa = input(f"Dammi una stringa: ")
lettera = input(f"Dammi lettera da controllare: ")

if stringa.startswith(lettera):
    print(f"{stringa} inizia con la lettera {lettera}")
else:
    print(f"{stringa} non inizia con la lettera {lettera}")

