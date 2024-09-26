"""
Script per togliere vocali da una stringa
"""

stringa = input("Dammi una stringa: ")

# rimuovo i caratteri ' ' con ''
stringa_senza_spazi = stringa.replace(' ', '')

print(f"La stringa senza spazi è {stringa_senza_spazi}")
