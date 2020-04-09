# 10996 별 찍기 - 21
if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print("*")
    else:
        for i in range(0, 2 * N):
            if i % 2 == 0:
                for j in range(0, N):
                    if j % 2 == 0:
                        print("*", end='')
                    else:
                        print(" ", end='')
            else:
                for j in range(0, N):
                    if j % 2 == 0:
                        print(" ", end='')
                    else:
                        print("*", end='')
            print()