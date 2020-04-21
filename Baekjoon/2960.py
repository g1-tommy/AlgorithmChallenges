# 2960 에라토스테네스의 체
def isPrime(num):
    p = True
    for _ in range(2, num):
        if num % _ == 0:
            p = False
            break
    return p

if __name__ == "__main__":
    N, k = map(int, input().split())
    uList = [el for el in range(2, N + 1)]
    count = 0
    target = None
    while count < k:
        cursor = uList[0]
        if isPrime(cursor):
            for _ in uList:
                if _ % cursor == 0:
                    target = _
                    uList.remove(_)
                    count += 1
                    if count == k:
                        break
    print(target)