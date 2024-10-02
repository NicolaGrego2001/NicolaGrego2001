"""
Script per raccogliere in una lista,
gli studenti insufficienti nella classe
"""

lista_di_dizionari = [
    {'nome': 'Simone', 'voto': 30},
    {'nome': 'Asdrubale', 'voto': 11},
    {'nome': 'Giammaria', 'voto': 22}
]

numero_studenti = len(lista_di_dizionari)

insufficienza = 17
studenti_insufficienti = []
for studente in lista_di_dizionari:
    if studente.get('voto') <= insufficienza:
        # siamo qui dentro se lo studente è insuff
        studenti_insufficienti.append(studente.get('nome'))

print(studenti_insufficienti)



# EQUIVALENTE
# for i in range(len(lista_di_dizionari)):
#     studente = lista_di_dizionari[i]
#     print(studente['voto'])