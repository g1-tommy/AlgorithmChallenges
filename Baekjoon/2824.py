# 2824 최대공약수
from math import gcd

if __name__ == "__main__":
    mul = [1, 1]
    for _ in range(2):
        N = int(input())
        numNs = list(map(int, input().split()))
        for i in numNs:
            mul[_] *= i
    mul.sort()
    tmp = gcd(*mul)
    if tmp > 10 ** 9:
        tmp = str(tmp)
        print(tmp[len(tmp) - 9:len(tmp)])
    else:
        print(tmp)