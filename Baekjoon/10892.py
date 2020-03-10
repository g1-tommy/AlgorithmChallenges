# 10872 팩토리얼
if __name__ == "__main__":
    fac = 1
    N = int(input())
    for i in range(N, 1, -1):
        fac *= i
    print(fac)