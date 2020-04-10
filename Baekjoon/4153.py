# 4153 직각삼각형
if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        sum = 0
        max = arr[0]
        for item in arr:
            sum += item
            if item > max:
                max = item
        if sum == 0:
            break
        arr.remove(max)
        lineSum = 0
        for item in arr:
            lineSum += item ** 2
        if lineSum == max ** 2:
            print("right")
        else:
            print("wrong")
        