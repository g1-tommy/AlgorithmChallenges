# 5622 다이얼
if __name__ == "__main__":
    times = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
    sum = 0
    for s in input():
        sum += times[ord(s) - 65]
    print(sum)