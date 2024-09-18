# online interpreter
# https://www.w3schools.com/Python/trypython.asp?filename=demo_compiler

# pycharm
# https://www.jetbrains.com/pycharm/download
# scendere sotto per la versione community

# scrivere funzione che prende in input due interi e ne calcola la somma

def somma(a: int, b: int) -> int:
    addizione = a + b
    return addizione


y = somma(3, 8)
print(f"La somma di 3 e 8 è: {y}")


# scrivere funzione che itera su una lista di stringhe e stampa 'ok!' ogni volta nell'elemento
# sia presente la parola 'simone'
listone = ['pippo', 'simone', 'francesco', 'alessandro', 'giuseppe']


def simone(list_of_names: list) -> None:
    for elemento in list_of_names:
        if elemento == 'simone':
            print('ok!')
    return


simone(listone)
simone(['pippo', 'simone', 'francesco', 'alessandro', 'giuseppe'])


# scrivere funzione che richiede (tramite psutil) la percentuale di CPU utilizzata ogni secondo,
# per cinque secondi e poi ne ritorna la media


def media_cpu(n_sec=5) -> float:
    import psutil
    lista_totale = []
    for i in range(n_sec):
        perc = psutil.cpu_percent(interval=1)
        lista_totale.append(perc)
    somma_perc = sum(lista_totale)
    n_tot = len(lista_totale)
    media = somma_perc / n_tot
    return media


print(media_cpu(1))

# data una lista di nomi di persone, scrivere una funzione che controlla se la prima lettera è maiuscola
# e se non lo è, stampa un avviso


def maiuscolo_check(lista_nomi_persone: list) -> None:
    for stringa in lista_nomi_persone:
        lettera_iniziale = stringa[0]
        if not lettera_iniziale.isupper():
            print("Avviso!11!!")


maiuscolo_check(['Pippo', 'Pluto', 'simone', 'Orlando', 'asdrubale'])

# scrivere una funzione che richiede all'utente 10 numeri e stampa ogni volta
# se il numero inserito è pari o dispari (operatore %)


def pari_o_dispari() -> None:
    for i in range(10):
        # chiediamo a utente di inserire un numero
        try:
            numero = int(input(f"{i}: Inserici un numero\n"))
        except ValueError:
            print(f"Hai sbagliato a scrivere... Try again")
            continue

        # controllare se è pari o dispari
        if numero % 2 == 0:
            # se la divisione tra il numero e due dà resto 0
            print(f"Numero pari")
        else:
            # se la divisione tra il numero e due dà resto diverso da 0 (cioè 1)
            print(f"Numero dispari")


# pari_o_dispari()

# scrivere una funzione che controlla se un parametro in input è una stringa.
# Se lo è ritorna True, se non lo è ritorna False

# isinstance(variabile, tipo)
# isinstance(var, str)


def is_str(var) -> bool:
    if isinstance(var, str):
        return True
    else:
        return False


print(is_str('pippo'))
print(is_str(1024))
# scrivere una funzione che ritorna quante volte la parola 'Simone' è presente
# all'interno di una stringa data in input alla funzione

# suggerimenti usare .replace(...)


def quanti_simoni(s: str) -> int:
    return s.count('Simone')


print(quanti_simoni('SimonesimoneSimonesimone'))
