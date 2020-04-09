# 1110 더하기 사이클
if __name__ == "__main__":
    N = int(input())
    t10 = 0
    t1 = 0
    newN = N
    count = 0
    while True:
        t10 = newN % 10
        t1 = (newN // 10 + newN % 10) % 10
        newN = t10 * 10 + t1
        count += 1
        if newN == N:
            break
    print(count)