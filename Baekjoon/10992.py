# 10992 별 찍기 - 17
if __name__ == "__main__":
    N = int(input())
    for _ in range(1, N):
        print(" " * (N - _), end='')
        print("*", end='')
        print(' ' * (2 * (_ - 1) - 1), end='')
        if _ != 1:
            print("*")
        else:
            print()
    print("*" * (2 * N - 1))