# scrivere funzione che prende in input due interi e ne calcola la somma

def somma(a: int, b: int) -> int:
    ...

# scrivere funzione che itera su una lista di stringhe e stampa 'ok!' ogni volta nell'elemento
# sia presente la parola 'simone'

def simone(l: list) -> None:
    ...

# scrivere funzione che richiede (tramite psutil) la percentuale di CPU utilizzata ogni secondo,
# per due minuti e poi ne calcola la media

def media_cpu() -> float:
    ...

# data una lista di nomi di persone, scrivere una funzione che controlla se la prima lettera è maiuscola e se non lo è,
# stampa un avviso

def maiuscolo_check(l: list) -> None:
    ...

# scrivere una funzione che richiede all'utente 10 numeri e stampa ogni volta
# se il numero inserito è pari o dispari

def pari_o_dispari() -> None:
    ...


# scrivere una funzione che controlla se un parametro in input è una stringa. Se lo è ritorna True, se non lo è
# ritorna False

def is_str(var) -> bool:
    ...

# scrivere una funzione che ritorna quante volte la parola 'Simone' è presente all'interno di una stringa in input
# suggerimenti usare .replace(...)

def quanti_simoni(s: str) -> int:
    ...