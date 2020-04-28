# 11652 카드
import sys
from collections import Counter
input = sys.stdin.readline
if __name__ == "__main__":
    collections = list()
    N = int(input())
    for _ in range(N):
        collections.append(int(input()))
    counter = Counter(collections).most_common()
    maxI = counter[0][-1]
    minV = 2 ** 62
    for idx, count in counter:
        if min(minV, idx) == idx and max(count, maxI) == count:
            maxI = count
            minV = idx
    print(minV)