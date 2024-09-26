"""
Script per contare il numero di vocali in una parola
"""

stringa = input("Dammi una stringa: ")

# creo una lista con tutte le vocali | potrei usare una stringa 'aeiouAEIOU', dato che in Python è iterabile

vocali = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# inizializzo una variabile intera a 0
conteggio_vocali = 0
# itero sui caratteri della stringa
for carattere in stringa:
    # se il carattere è presente nella lista delle vocali
    if carattere in vocali:
        # aggiungo uno al conteggio delle vocali
        conteggio_vocali += 1

# stampo il conteggio delle vocali
print(f"Ci sono {conteggio_vocali} vocali nella stringa {stringa}")
