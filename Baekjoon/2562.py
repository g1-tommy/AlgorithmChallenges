# 2562 최댓값
if __name__ == "__main__":
    max = 0
    index = None
    arr = []
    for i in range(9):
        arr.append(int(input()))
    for idx, item in enumerate(arr):
        if (item > max):
            max = item
            index = idx
    print(max)
    print(index + 1)