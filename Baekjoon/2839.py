# 2839 설탕 배달
if __name__ == "__main__":
    N = int(input())
    count = 0
    while N > 0:
        if N % 5 == 0:
            count += 1
            N -= 5
        elif N % 3 == 0:
            count += 1
            N -= 3
        elif N > 5:
            count += 1
            N -= 5
        else:
            count = -1
            break
    print(count)