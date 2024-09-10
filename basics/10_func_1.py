# scrivere una funzione che calcola se un numero in input è pari
# sapendo

# for
# while
# if
# +, -, *, /
# // (divisione intera) -> 5//2 = 2
# % (resto da divisione intera) -> 5 % 2 = 1

# isinstance(var1, int) -> True se var1 è intero
# isinstance(var2, float)

def pari(n: int) -> bool:
    resto = n % 2
    if resto == 0:
        return True
    else:
        return False


def dispari(n: int) -> bool:
    return not pari(n)


print(pari(3))