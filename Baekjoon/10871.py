# 10871 X보다 작은 수
if __name__ == "__main__":
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in arr:
        if (i < X):
            print(i, end=' ')