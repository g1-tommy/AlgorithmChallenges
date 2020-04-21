# 2501 약수 구하기
if __name__ == "__main__":
    N, K = map(int, input().split())
    exists = False
    count = 0
    for _ in range(1, N + 1):
        if N % _ == 0:
            count += 1
            if count == K:
                exists = True
                print(_)
                break
    if not exists:
        print(0)