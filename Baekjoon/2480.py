# 2480 주사위 세개
from collections import Counter
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    cSet = set(nums)
    if len(cSet) == 1:
        print(10000 + list(cSet)[0] * 1000)
    elif len(cSet) == 2:
        tmp = Counter(nums)
        print(1000 + list(filter(lambda x: tmp[x] == 2, tmp))[0] * 100)
    else:
        print(sorted(nums)[-1] * 100)