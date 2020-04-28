# 10991 별 찍기 - 16
if __name__ == "__main__":
    N = int(input())
    for _ in range(1, N + 1):
        print(" " * (N - _), end='')
        print("* " * (_ - 1), end='')
        print("*")