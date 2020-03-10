# 2675 문자열 반복
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        retn = ''
        length, string = input().split()
        for j in string:
            retn += j * int(length)
        print(retn)