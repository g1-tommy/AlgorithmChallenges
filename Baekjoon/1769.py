# 1769 3의 배수
if __name__ == "__main__":
    N = list(map(int, input()))
    count = 0
    while len(N) > 1:
        tmp = sum(N)
        count += 1
        N = list(map(int, str(tmp)))
    print(count)
    print('YES' if N[-1] % 3 == 0 else 'NO')