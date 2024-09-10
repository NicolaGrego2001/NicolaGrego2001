import random
import time

from cachetools import cached, TTLCache

def get_results() -> int:
    time.sleep(1)  # simuliamo che ci voglia un secondo a fare il calcolo
    return int(time.time() // 5)

@cached(cache=TTLCache(maxsize=128, ttl=5))
def get_results_cached() -> int:
    time.sleep(1)
    return int(time.time() // 5)
def main():
    for i in range(10):
        #print(get_results())
        print(get_results_cached())
    time.sleep(7)
    for i in range(10):
        #print(get_results())
        print(get_results_cached())

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Tempo di esecuzione: {time.perf_counter() - start} secondi")