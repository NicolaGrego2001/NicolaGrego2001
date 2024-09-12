from time import perf_counter
from functools import lru_cache


def sum_all_numbers_upto(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


@lru_cache(maxsize=128)
def sum_all_numbers_upto_cached(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


def no_cache() -> None:
    print(f"Faccio le prime operazioni")
    print(f"Calcolo la somma")
    print(sum_all_numbers_upto(100_000_000))
    print(f"Faccio altre operazioni")
    print(sum_all_numbers_upto(100_000_000))
    print(f"Faccio altre operazioni ancora")
    print(sum_all_numbers_upto(100_000_000))
    print(f"Finito")


def with_cache() -> None:
    print(f"Faccio le prime operazioni")
    print(f"Calcolo la somma")
    print(sum_all_numbers_upto_cached(100_000_000))
    print(f"Faccio altre operazioni")
    print(sum_all_numbers_upto_cached(100_000_000))
    print(f"Faccio altre operazioni ancora")
    print(sum_all_numbers_upto_cached(100_000_000))
    print(f"Finito")


def main():
    start = perf_counter()
    # no_cache()
    with_cache()
    print(f"Ci ho messo {perf_counter() - start}s")


if __name__ == '__main__':
    main()
