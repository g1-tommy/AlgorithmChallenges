# 11050 이항 계수 I
if __name__ == "__main__":
    N, K = map(int, input().split())
    base = 1
    for i in range(1, N + 1):
        base *= i
    for i in range(K, 0, -1):
        base //= i
    for i in range(N - K, 0, -1):
        base //= i
    print(base)