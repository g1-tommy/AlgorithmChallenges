# 11721 열 개씩 끊어 출력하기
if __name__ == "__main__":
    N = input()
    strList = list()
    while len(N) > 0:
        strList.append(N[0:10])
        N = N[10:]
    for item in strList:
        print(item)