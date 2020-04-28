# 2525 오븐 시계
if __name__ == "__main__":
    H, M = map(int, input().split())
    duration = int(input())
    M += duration % 60
    H += duration // 60
    if M >= 60:
        M -= 60
        H += 1
    if H >= 24:
        H -= 24
    print(H, M)