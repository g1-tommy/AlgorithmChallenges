# 1271 엄청난 부자2
if __name__ == "__main__":
    N, M = map(int, input().split())
    print(N // M)
    print(N - N // M * M)