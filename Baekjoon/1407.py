# 1407 2로 몇 번 나누어질까
def f(num):
    r = num
    i = 0
    while True:
        i += 1
        if 2 ** i > num:
            break
        r += (num // (2 ** i)) * ((2 ** i) // 2)
    return r

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(f(B) - f(A-1))