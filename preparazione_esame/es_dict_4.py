"""
Script per raccogliere in una lista,
gli studenti che hanno almeno un'insufficienza
"""

lista_di_dizionari = [
    {'nome': 'Simone', 'voti': [30, 27, 21, 18]},
    {'nome': 'Asdrubale', 'voti': [11, 18, 22, 30]},
    {'nome': 'Giammaria', 'voti': [22, 15, 14, 11]}
]

# prima possibilità
insufficienza = 17
studenti_insufficienti = []
for studente in lista_di_dizionari:
    insufficiente = False
    nome = studente.get('nome')
    voti = studente.get('voti')
    for voto in voti:
        if voto <= insufficienza:
            insufficiente = True
    if insufficiente:
        studenti_insufficienti.append(nome)

print(studenti_insufficienti)

# seconda possibilità
insufficienza = 17
studenti_insufficienti = []
for studente in lista_di_dizionari:
    nome = studente.get('nome')
    voti = studente.get('voti')
    for voto in voti:
        if voto <= insufficienza:
            studenti_insufficienti.append(nome)
            break

print(studenti_insufficienti)

# terza possibilità
insufficienza = 17
studenti_insufficienti = []
for studente in lista_di_dizionari:
    nome = studente.get('nome')
    voti = studente.get('voti')
    for voto in voti:
        if voto <= insufficienza:
            studenti_insufficienti.append(nome)

print(list(set(studenti_insufficienti)))




# EQUIVALENTE
# for i in range(len(lista_di_dizionari)):
#     studente = lista_di_dizionari[i]
#     print(studente['voto'])