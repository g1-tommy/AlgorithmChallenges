# 1712 손익분기점
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    start = -1
    if C > B:
        start = A // (C - B) + 1
    print(start)