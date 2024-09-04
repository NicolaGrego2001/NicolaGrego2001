# scrivere funzione che riceve in input una lista di valori e li scrive nel file
# output.txt


def write_list(lista) -> None:
    file_to_write = 'output.txt'
    with open(file_to_write, 'wt') as prova:
        for elemento in lista:
            # if isinstance(elemento, int) or isinstance(elemento, float):
            #    continue
            prova.write(f'{elemento}\n')


lista = ['fsfds', 2, 'fdsbfdsbfdsnja', True, 4.1]

write_list(lista)
