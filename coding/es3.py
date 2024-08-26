# siccome tutto in python è un oggetto, non stupisce che anche gli int e compagnia abbiamo degli attributi e dei metodi che possiamo
# utilizzare. La notazione per accedere a metodi e attributi di un oggetto è la dotted notation.

stringa1: str = 'Pippo'
intero1: int = 10

# distinguere metodi da attributi è semplice (lasciamoci aiutare dal nostro IDE).

# Gli attributi sono "valori" e in quanto valori non mostrano le parentesi (tipiche delle funzioni)

print(intero1.real)


# mentre i metodi (in quanto funzioni) sono richiamate con le parentesi (eventualmente specificando parametri)

print(stringa1.lower())

print(stringa1.startswith('F'))