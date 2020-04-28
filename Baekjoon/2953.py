# 2953 나는 요리사다
if __name__ == "__main__":
    scores = list()
    maxUser = 0
    for _ in range(5):
        score = list(map(int, input().split()))
        if len(scores) == 0:
            maxUser = _ + 1
        else:
            if max(scores) < sum(score):
                maxUser = _ + 1
        scores.append(sum(score))
    print(maxUser, max(scores))
    