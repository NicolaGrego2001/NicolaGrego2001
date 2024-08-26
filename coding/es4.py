# il mondo non è fatto solo di interi, di stringe e di floats, ma ci sono casi in cui ci servono degli oggetti più complessi.

# python ci mette a disposizione tre tipi (che in python sono ancora considerati primitivi -> built-ins)

list
dict
tuple

# torniamo alle slides

# bentornati

# definiamo una stringa
stringa1: str = 'Ciao'
# se vogliamo aggiungere contenuto a una stringa possiamo servirci dell'operatore +

stringa1 += '!'

# tuttavia l'operatore + non aggiunge contenuto alla variabile stringa1
print(stringa1)
# bensì crea un nuovo oggetto di tipo stringa. Per conservare il risultato, dobbiamo salvarlo all'interno di una nuova variabile

stringa2 = stringa1 + '!'
print(stringa1)
print(stringa2)

# se spulciamo i metodi supportati dall'oggetto str vediamo che ce n'è uno chiamato .replace(...). Forse quello modifica direttamente
# la stringa1 piuttosto che crearne una nuova?
stringa1.replace('a', 'o')
print(stringa1)

# no, neanche questo
stringa3 = stringa1.replace('a', 'o')
print(stringa3)

# in ogni caso che possiamo trovare il contenuto della stringa originale stringa1 rimane immutato. Non sorprende forse che
# l'oggetto str appartiene a una categoria di oggetti python chiamati Immutable, cioè immutabili.

# Questo indica che ogni operazione che comporterebbe la modifica della stringa originale, in realtà genera un nuovo oggetto
# di tipo str frutto della copia della stringa originale con appunto le modifiche che gli abbiamo voluto fare.

# Se vogliamo modificarne il contenuto in-place (cioè mantenendo un singolo oggetto in memoria dobbiamo usare la notazione che autoreferenzia la stringa


stringa1 = stringa1.replace('a', 'o')
print(stringa1)

# oppure, se stiamo aggiungendo contenuto
stringa1 = 'Ciao'
stringa1 = stringa1 + '!'
print(stringa1)

# oppure semplificando la notazione
stringa1 += '!'
print(stringa1)

# in tutti i casi python copia il contenuto della stringa1 in un nuovo oggetto (a cui fa le modifiche necessarie) e cambia
# il reference dell'etichetta stringa1 sul nuovo oggetto, cancellando quello precedente. È un'operazione che comporta un dispendio
# di risorse "inutili". Per cui quando utilizziamo degli oggetti immutable dobbiamo pensarci un paio di volte prima di modificarlo

# cosa c'entra questo con le liste, perchè di liste stavamo parlando

# la differenza è che una lista, invece è un oggetto della categoria Mutable. Ossia è un oggetto a cui è permesso mutare.

# questo rende più comodo per esempio aggiungere contenuto a una lista

lista = [1, 2, 3]

print(lista)
lista.append(4)
print(lista)

# ma questo può avere degli effetti inaspettati

stringa_dentro = 'Dentro'
lista = [1, 2, 3, stringa_dentro]

print(lista)

stringa_dentro += ' o Fuori'
print(stringa_dentro)

print(lista)

# le modifiche che ho fatto alla stringa_dentro non si sono propagate all'interno della lista dove l'ho inserita.
# questo perchè la stringa è immutable. Quindi python ha creato un nuovo oggetto per creare la nuova stringa. Essendo un nuovo oggetto,
# quello all'interno della lista è rimasto immutato.

# diverso sarebbe stato se al posto che una stringa, avessi inserito una lista nested (cioè innestata dentro la lista principale)

lista_dentro = [4]

lista = [1, 2, 3, lista_dentro]

print(lista)

lista_dentro.append(5)

print(lista)

# quello che vogliamo evidenziare è che bisogna sempre tenere presente con che tipi di oggetti stiamo lavorando e, in
# particolare se parliamo di oggetti immutable o mutable

# torniamo alle slides

