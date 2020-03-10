# 4344 평균은 넘겠지
if __name__ == "__main__":
    C = int(input())
    for i in range(C):
        arr = list(map(int, input().split()))
        count = arr[0]
        cases = arr[1:]
        avg = sum(cases) / len(cases)
        overAvg = list(map(lambda x: x > avg, cases))
        print("%.3f" % (round(overAvg.count(True) / count * 100, 3)) + '%')