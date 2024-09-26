# ERRORI

nome: str = "Pippo"
numero_intero: int = 10
booleano: bool = True
numero_virgola_mobile: float = 10.0


# quando viene fatta un'operazione che non è possibile fare, python "solleva" un ECCEZIONE

#non_somma = numero_intero + nome

# le eccezioni non previste portano a un'interruzione del programma.
# se ci aspettiamo che una parte di codice possa portare a un'eccezione o, in altre parole, a un errore
# possiamo decidere se lasciare crashare il programma oppure se prevedere delle operazioni da fare nel caso d'errore

try:
    non_somma = numero_intero + nome
except Exception as e:
    print("Si è verificato un errore durante la somma:", e)
    non_somma = numero_intero

print(non_somma)

# non bisogna essere troppo generici con gli errori che ci aspettiamo (Exception raggruppa un po' tutti i possibili
# errori che possono succedere). È sempre molto, ma MOLTO MEGLIO catchare errori specifici per i quali si scrive del
# codice per porre rimedio. In questo caso viene sollevata un'eccezione del tipo TypeError, per cui meglio catchare
# quel tipo di errore

try:
    non_somma = numero_intero + nome
except TypeError as e:
    print("Si è verificato un errore durante la somma:", e)
    non_somma = numero_intero