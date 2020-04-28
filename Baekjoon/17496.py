# 17496 스타후르츠
if __name__ == "__main__":
    N, T, C, P = map(int, input().split())
    count = 0
    tmp = 0
    ableToGrow = True
    for i in range(1, N + 1):
        if i == tmp:
            ableToGrow = True
            tmp = 0
            count += C
        if ableToGrow:
            ableToGrow = False
            tmp = i + T
    print(P * count)