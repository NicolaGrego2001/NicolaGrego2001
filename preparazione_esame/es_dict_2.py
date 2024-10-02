"""
Script per calcolare voto massimo della classe
"""

lista_di_dizionari = [
    {'nome': 'Simone', 'voto': 30},
    {'nome': 'Asdrubale', 'voto': 18},
    {'nome': 'Giammaria', 'voto': 22}
]

numero_studenti = len(lista_di_dizionari)

massimo = 0
for studente in lista_di_dizionari:
    if massimo < studente.get('voto'):
        massimo = studente.get('voto')

    # if massimo > studente.get('voto'):
    #     continue
    # else:
    #     massimo = studente.get('voto')

print(massimo)



# EQUIVALENTE
# for i in range(len(lista_di_dizionari)):
#     studente = lista_di_dizionari[i]
#     print(studente['voto'])