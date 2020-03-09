# 15552 빠른 A+B
import sys

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        print(sum(arr))