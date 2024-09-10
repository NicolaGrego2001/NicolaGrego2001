# online interpreter
# https://www.w3schools.com/Python/trypython.asp?filename=demo_compiler

# pycharm
# https://www.jetbrains.com/pycharm/download
# scendere sotto per la versione community

# scrivere funzione che prende in input due interi e ne calcola la somma

def somma(a: int, b: int) -> int:
    result = a + b
    return result


print(f"somma(1, 2) -> {somma(1, 2)}")


# scrivere funzione che itera su una lista di stringhe e stampa 'ok!' ogni volta nell'elemento
# sia presente la parola 'simone'

def simone(l: list) -> None:
    for stringa in l:
        if 'simone' in stringa:
            print("ok!")
    return


print(f"Eseguo simone(['pippo', 'pluto', 'simone', 'simoncino', 'simonello'])")
simone(['pippo', 'pluto', 'simone', 'simoncino', 'simonello'])

# scrivere funzione che richiede (tramite psutil) la percentuale di CPU utilizzata ogni secondo,
# per due minuti e poi ne calcola la media

def media_cpu() -> float:
    import psutil
    import time
    minuti = 2
    secondi = 2 * 60
    cpu_usages = []
    for i in range(secondi):
        cpu_usages.append(psutil.cpu_percent(interval=1))
        # psutil raccoglie comunque informazioni per un secondo
        # non ho bisogno di attendere che passi il secondo
        # time.sleep(1)
    # calcolo media
    media = sum(cpu_usages) / len(cpu_usages)
    return media


print(f"Media CPU: {media_cpu()}")

# data una lista di nomi di persone, scrivere una funzione che controlla se la prima lettera è maiuscola e se non lo è,
# stampa un avviso

def maiuscolo_check(l: list) -> None:
    for nome in l:
        if not nome[0].isupper():
            print(f"Nome '{nome}' non inizia con una lettera maiuscola")
        # posso anche fare
        # if nome[0].upper() != nome[0]:
        #    print(f"Nome '{nome}' non inizia con una lettera maiuscola")
    return None


print(f"maiuscolo_check(['Giovanni', 'Francesco', 'Isaia', 'enea', 'Simone'])")
maiuscolo_check(['Giovanni', 'Francesco', 'Isaia', 'enea', 'Simone'])

# scrivere una funzione che richiede all'utente 10 numeri e stampa ogni volta
# se il numero inserito è pari o dispari

def pari_o_dispari() -> None:
    for i in range(10):
        num = int(input(f"Dammi un numero:\n"))
        if num % 2 == 0:
            print(f"Il numero {num} è pari")
        else:
            print(f"Il numero {num} è dispari")
    return

print(f"Interazione con utente pari_o_dispari()")
pari_o_dispari()


# scrivere una funzione che controlla se un parametro in input è una stringa. Se lo è ritorna True, se non lo è
# ritorna False

def is_str(var) -> bool:
    return isinstance(var, str)


print(f"is_str('pippo') -> {is_str('pippo')}")
print(f"is_str(123) -> {is_str(123)}")

# scrivere una funzione che ritorna quante volte la parola 'Simone' è presente all'interno di una stringa in input
# suggerimenti usare .replace(...)

def quanti_simoni(s: str) -> int:
    n_simoni: int = 0
    stop = False
    while not stop:
        if 'Simone' in s:
            n_simoni += 1
            s = s.replace('Simone', '', 1)
        if 'Simone' not in s:
            stop = True
    return n_simoni

print(f"quanti_simoni('Simone chiese agli studenti se potevano scrivere uno script per contare il numero di Simoni in una stringa contenente tanti simoni')")
print(quanti_simoni('Simone chiese agli studenti se potevano scrivere uno script per contare il numero di Simoni in una stringa contenente tanti simoni'))
