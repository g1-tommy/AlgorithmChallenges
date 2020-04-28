# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰
if __name__ == "__main__":
    compare = [1,1,2,2,2,8]
    uInput = list(map(int, input().split()))
    for idx, val in enumerate(compare):
        print(val - uInput[idx], end=' ')
    print()