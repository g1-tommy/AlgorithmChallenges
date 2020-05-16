# 1748 수 이어 쓰기 1
from math import log10, floor
if __name__ == "__main__":
    N = int(input())
    tmp = floor(log10(N))
    length = 0
    for _ in range(1, (tmp + 1) + 1):
        if _ != tmp + 1:
            length += 9 * (10 ** (_ - 1)) * _
        else:
            length += (N - (10 ** (_ - 1)) + 1) * _
    print(length)