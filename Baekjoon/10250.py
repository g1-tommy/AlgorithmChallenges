# 10250 ACM 호텔
"""
풀이: 특징 파악
좌측 하단부터 상향으로 방 배정
따라서 층 수는 N % H이며 N % H == 0 일 경우 H로 설정
호수는 N // H + 1이며 N % H == 0 일 경우 기존값-1로 설정
"""
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        H, W, N = map(int, input().split())
        floor = N % H
        dist = N // H + 1
        if floor == 0:
            floor = H
            dist -= 1
        print(floor * 100 + dist)