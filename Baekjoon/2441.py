# 2441 별 찍기 - 4
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(i * " ", (N - i) * "*", sep="")