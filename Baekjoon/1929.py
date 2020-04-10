# 1929 소수 구하기
if __name__ == "__main__":
    M, N = map(int, input().split())
    for i in range(M, N + 1):
        isPrime = True
        # 소수 판별법: sqrt(n)에 대해서만 이상 없을 경우 소수
        for j in range(2, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if i != 1 and isPrime:
            print(i)