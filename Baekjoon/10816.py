# 10816 숫자 카드 2
"""
풀이: Hashmap 이용
"""
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    compareSet = list(map(int, input().split()))
    counter = dict()
    for item in cards:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    print(" ".join(str(counter[item]) if item in counter else '0' for item in compareSet))
