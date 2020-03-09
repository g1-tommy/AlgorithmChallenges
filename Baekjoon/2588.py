# 2588 곱셈
if __name__ == "__main__":
    arr = []
    while True:
        try:
            temp = int(input())
        except:
            break
        else:
            arr.append(temp)

    unit = [(arr[-1] - (arr[-1] % 100)) // 100, (arr[-1] - ((arr[-1] // 100) * 100) - (arr[-1] % 10)) // 10, arr[-1] % 10]
    unit.reverse()
    for i in unit:
        print(arr[0] * i)
    print(arr[0] * arr[-1])