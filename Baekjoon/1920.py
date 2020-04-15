# 1920 수 찾기
"""
풀이 : Hashmap 이용
"""
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    compareSet = list(map(int, input().split()))
    M = int(input())
    findSet = list(map(int, input().split()))
    
    checker = dict()
    for item in compareSet:
        checker[item] = True
    for item in findSet:
        if item in checker:
            print(1)
        else:
            print(0)