# 2164 카드2
"""
풀이:
N = 1인 케이스부터 차례로 결과값 나열시 규칙성 발견
N = 2^ceil(log2(N)) - 2 * (2^ceil(log2(N)) - N)
"""
from math import log2, ceil
if __name__ == "__main__":
    N = int(input())
    print(2**ceil(log2(N)) - 2 * (2**ceil(log2(N)) - N))