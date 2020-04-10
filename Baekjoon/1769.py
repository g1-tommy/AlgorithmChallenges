# 1769 3의 배수
if __name__ == "__main__":
    N = int(input())
    temp = str(N)
    count = 0
    while int(temp) >= 10:
        count += 1
        tSum = 0
        for item in temp:
            tSum += int(item)
        if tSum % 3 == 0 or tSum < 10:
            break
        temp = str(tSum)
    print(count)
    if int(temp) % 3 == 0:
        print("YES")
    else:
        print("NO")