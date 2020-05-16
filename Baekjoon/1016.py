# 1016 제곱ㄴㄴ수
"""
풀이 : 에라토스테네스의 체
"""
if __name__ == "__main__":
    min, max = map(int, input().split())
    N = 1
    count = 0
    sieve = [True] * (max - min + 1)
    while N ** 2 <= max:
        N += 1
        tmp = N ** 2
        i = min // tmp
        while tmp * i <= max:
            idx = tmp * i - min
            if idx >= 0 and sieve[idx]:
                count += 1
                sieve[idx] = False
            i += 1
    print(len(sieve) - count)