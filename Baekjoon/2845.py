# 2845 파티가 끝나고 난 뒤
if __name__ == "__main__":
    L, P = map(int, input().split())
    media = list(map(int, input().split()))
    for item in media:
        print(item - L*P, end=' ')
    print()