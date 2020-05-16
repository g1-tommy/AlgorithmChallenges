# 1377 버블 소트
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    arr = list()
    for _ in range(N):
        arr.append((int(input()), _))
    sortedArr = sorted(arr)
    answer = []
    for _ in range(N):
        answer.append(sortedArr[_][-1] - arr[_][-1])
    print(max(answer) + 1)