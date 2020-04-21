# 2581 소수
from math import sqrt
def prime(num):
    tmp = True
    for _ in range(2, int(sqrt(num)) + 1):
        if num % _ == 0:
            tmp = False
            break
    return tmp

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    primeList = [_ for _ in range(M, N + 1) if prime(_)]
    if 1 in primeList:
        primeList.remove(1)
    if len(primeList) == 0:
        print(-1)
    else:
        print(sum(primeList))
        print(min(primeList))