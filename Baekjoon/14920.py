# 14920 3n+1 수열
if __name__ == "__main__":
    N = int(input())
    count = 1
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
        count += 1
    print(count)