# 2446 별 찍기 - 9
if __name__ == "__main__":
    N = int(input())
    s = -1
    t = 2 * N + 1
    for i in range(0, 2 * N - 1):
        if i < N:
            s += 1
            t -= 2
        else:
            s -= 1
            t += 2
        print(" " * s, "*" * t, sep='')
