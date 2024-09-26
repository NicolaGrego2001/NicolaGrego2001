# VARIABILI, KEYWORD, BASIC FLOW

# in questo script vediamo le basi della sintassi di python

# per aprire una sessione di interprete di python basta scrivere
# > python3 sul terminale

# Se si vuole eseguire uno script già scritto, basta scrivere
# > python3 file.py

# siccome siamo nel 2024 ed è ormai buona norma, utilizzerò il type hinting ovunque sia possibile.
# valgono le considerazioni fatte prima: il type hinting è un hinting

# per assegnare delle variabili utilizziamo l'operatore =

nome = "Pippo"
numero_intero = 10
booleano = True
numero_virgola_mobile = 10.0

# usando il type hinting
nome: str = "Pippo"
numero_intero: int = 10
booleano: bool = True
numero_virgola_mobile: float = 10.0

# per stampare una variabile (o un qualsiasi oggetto) volessimo stampare a schermo, possiamo usare la
# FUNZIONE print()

print(nome)

# la funzione print accetta altri argomenti

print(nome, numero_intero)

print(nome, numero_intero, sep='|')
print(nome, numero_intero, sep='|', end='STOP')

# per visualizzare il tipo di una variabile utilizziamo la funzione type()

print(type(nome))
print(type(numero_virgola_mobile))

# per assegnare a una nuova variabile il risultato di una operazione

somma = numero_intero + numero_virgola_mobile


print(somma)
# vedete il casting?

# se proviamo a fare una somma di stringhe cosa esce fuori?

stringa1 = 'pippo'
stringa2 = 'pluto'
print(stringa1 + stringa2)

# l'operatore + nel caso di stringhe rappresenta l'operatore di concatenazione

# se vogliamo porre una condizione possiamo usare il costrutto
# if (condizione):
#   fai operazione
# elif (altra condizione):
#   fai altra operazione
# else:
#   fai altra opeazione ancora
#

if numero_intero < 10:
    print("Il numero è minore di 10")
elif numero_intero > 10:
    print("Il numero è maggiore di 10")
else:
    print("Il numero è uguale a 10")

# in python è OBBLIGATORIO INDENTARE IL CODICE
# in altri linguaggi è solo suggerito come modo per tenere ordinato il codice. Qui no -> IndentationError
#if numero_intero == 10:
#print(numero_intero)

# l'if non permette di ripetere l'operazione se una condizione non viene verificata. Questo è il lavoro del keyword while
n = 0
while n < 10:
    n = n + 1
print(n)

# se non ci interessa il controllo diretto di un valore e vogliamo semplicemente fare un'operazione un certo numero di volte
# possiamo servirci di un for loop

for i in range(10):  # per ogni elemento i all'interno del range(10) -> sottointeso da 0
    print('Devo studiare')

# quell'i non è solamente un modo per iterare ma è proprio un valore. Tra poco vedremo cosa fa quel range per capire
for i in range(10):
    print(i)

# il for loop è uno degli strumenti più utili della programmazione, in python anche di più

# possiamo definire una funzione con il keywork def

def somma_due_numeri(a: int, b: int) -> int:
    return a + b

# una volta definita è un concetto astratto, ma che possiamo richiamare con il nome della funzione e le parentesi per identificare
# i parametri se ce ne sono

print(somma_due_numeri(10, 20))

# una funzione, quindi accetta in input dei parametri e ritorna un output

print(type(somma_due_numeri(20, 30)))

# se prevediamo che una funzione non ritorni un output definito, ma ci basta che il suo codice venga eseguito, possiamo
# evitare di scrivere il return. In tal caso l'output sarà di tipo NoneType, cioè None (che rappresenta l'assenza di un valore)

def funzione_che_non_ritorna_nulla(a: int, b: str) -> None:
    print("Sto stampando, ma la funzione comunque non uscirà nulla")
    return  # sempre meglio mettere il return, comunque. Da ordine al codice e permette di capire al volo dove finisce

funzione_che_non_ritorna_nulla(100, 'blu')

print(funzione_che_non_ritorna_nulla(200, 'rosso'))
print(type(funzione_che_non_ritorna_nulla(300, 'giallo')))

