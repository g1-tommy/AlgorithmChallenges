# 5532 방학 숙제
from math import ceil
if __name__ == "__main__":
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(L - max(ceil(A / C), ceil(B / D)))