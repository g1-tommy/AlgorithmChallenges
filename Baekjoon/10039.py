# 10039 평균 점수
if __name__ == "__main__":
    sum = 0
    for i in range(5):
        score = int(input())
        if score < 40:
            sum += 40
        else:
            sum += score
    print(sum // 5)