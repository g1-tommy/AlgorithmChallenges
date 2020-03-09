# 2439 별 찍기 - 2
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(' ' * (N - (i + 1)), end='')
        print('*' * (i + 1))