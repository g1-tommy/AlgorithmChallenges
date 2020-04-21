# 10773 제로
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    K = int(input())
    uList = list()
    for _ in range(K):
        uInput = int(input())
        if uInput == 0:
            if len(uList) > 0:
                uList.pop()
            else:
                pass
        else:
            uList.append(uInput)
    print(sum(uList))