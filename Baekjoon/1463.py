# 1463 1로 만들기
"""
풀이: DP 이용
"""
if __name__ == "__main__":
    N = int(input())
    counter = [0 for _ in range(N + 1)]
    counter[0] = None
    counter[1] = 0
    for _ in range(2, N + 1):
        counter[_] = counter[_ - 1] + 1
        if _ % 3 == 0:
            counter[_] = min(counter[_], counter[_ // 3] + 1)
        elif _ % 2 == 0:
            counter[_] = min(counter[_], counter[_ // 2] + 1)
    print(counter[-1])