# 2523 별 찍기 - 13
if __name__ == "__main__":
    N = int(input())
    t = 0
    for i in range(0, 2 * N - 1):
        if i > N - 1:
            t -= 1
        else:
            t += 1
        print("*" * t)