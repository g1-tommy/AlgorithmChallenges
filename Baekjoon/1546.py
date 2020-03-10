# 1546 평균
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(N):
        arr[i] = arr[i] / arr[N - 1] * 100
    print(sum(arr) / N)