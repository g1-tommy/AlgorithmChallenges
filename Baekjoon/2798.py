# 2798 블랙잭
if __name__ == "__main__":
    N, limitSum = map(int, input().split())
    cards = list(map(int, input().split()))
    sum = 0
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if cards[i] + cards[j] + cards[k] > limitSum:
                    continue
                else:
                    sum = max(sum, cards[i] + cards[j] + cards[k])
    print(sum)