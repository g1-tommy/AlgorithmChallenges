# 2475 검증수
if __name__ == "__main__":
    sum = 0
    uNums = list(map(int, input().split()))
    for item in uNums:
        sum += item ** 2
    print(sum % 10)