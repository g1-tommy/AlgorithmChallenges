# 10870 피보나치 수 5
def nthFibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nthFibo(n-1) + nthFibo(n-2)

if __name__ == "__main__":
    print(nthFibo(int(input())))