# 3052 나머지
if __name__ == "__main__":
    count = 0
    arr = [0 for i in range(42)]
    for i in range(10):
        arr[int(input()) % 42] += 1
    for i in arr:
        if i != 0:
            count += 1
    print(count)