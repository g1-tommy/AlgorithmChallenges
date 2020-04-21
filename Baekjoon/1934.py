# 1934 최소공배수
from math import gcd
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(A * B // gcd(A, B))