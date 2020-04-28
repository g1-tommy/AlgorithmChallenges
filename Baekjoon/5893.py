# 5893 17배
if __name__ == "__main__":
    uInput = 0
    tmp = 0
    cInput = list(reversed(input()))
    for _ in cInput:
        uInput += 2 ** tmp * int(_)
        tmp += 1
    N = uInput * 17
    print(bin(N)[2:])