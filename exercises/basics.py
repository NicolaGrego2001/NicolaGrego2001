marca = 'opel'
anno_produzione = 2012
lifespan = 20
anno_rottamazione = anno_produzione + lifespan

cilindrata = 1.4

diesel = False
benzina = True


# scrivere dizionario in cui conservare i vostri dati anagrafici (nome e cognome)
# e l'elenco di social al quale siete iscritti.

dettagli = {

}
# considero la prima lettera
# l'ho già vista?
# se non l'ho vista la aggiungo al regsitro
# aumento di uno il numero di conteggi per la lettera

# scrivere dizionario con conteggio lettere nel vostro nome e cognome
# (Pippo -> {'p': 3, 'i': 1, 'o': 1}
#
nome = 'MaSsimiliano'.lower()
conteggio = {

}
"""
for char in nome:
    if char not in lettere_viste.keys():
        lettere_viste[char] = 1
    else:
        lettere_viste[char] += 1

print(lettere_viste)
"""

# versione count
from string import ascii_lowercase

conteggio = {}
for char in nome:
    if char not in conteggio.keys():
        conteggio[char] = 1
    else:
        conteggio[char] += 1

conteggio = {}
for char in ascii_lowercase:
    n_chars = nome.count(char)
    if n_chars == 0:
        continue
    conteggio[char] = n_chars

#print(conteggio)

# esercizio: scrivere il vostro nome in notazione CamelCase
nome = 'simone'
nome_list = list(nome)

for index, char in enumerate(nome_list):
    # index -> indice della lista
    # char -> carattere della lista
    if index % 2 == 0:
        # pari
        nome_list[index] = nome_list[index].lower()
    else:
        # dispari
        nome_list[index] = nome_list[index].upper()
risultato = 'SiMoNe'