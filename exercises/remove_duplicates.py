# scrivere uno script che prenda 10 interi dall'utente
# (input) e ritorni una lista di numeri senza duplicati

set_numeri = set()
for i in range(10):
    val = int(input('Dammi un numero:\n'))
    set_numeri.add(val)

print(set_numeri)

print(sum(set_numeri) / len(set_numeri))

