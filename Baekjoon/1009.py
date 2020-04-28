# 1009 분산 처리
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        tmp = a
        u = list()
        a %= 10
        u.append(a)
        while True:
            a *= tmp
            a %= 10
            if a in u:
                break
            else:
                u.append(a)
        if u[b % len(u) - 1] == 0:
            print(10)
        else:
            print(u[b % len(u) - 1])