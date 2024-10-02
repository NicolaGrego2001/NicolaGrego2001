"""
Script per calcolare media dei voti della classe
"""

lista_di_dizionari = [
    {'nome': 'Simone', 'voto': 30},
    {'nome': 'Asdrubale', 'voto': 18},
    {'nome': 'Giammaria', 'voto': 22}
]

numero_studenti = len(lista_di_dizionari)

totale_voti = 0
for studente in lista_di_dizionari:
    totale_voti += studente.get('voto')

print(totale_voti/numero_studenti)


# EQUIVALENTE
# for i in range(len(lista_di_dizionari)):
#     studente = lista_di_dizionari[i]
#     print(studente['voto'])