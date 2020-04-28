# 2193 이친수
if __name__ == "__main__":
    N = int(input())
    pinaries = [1, 1]
    for _ in range(2, N):
        pinaries.append(pinaries[-1] + pinaries[-2])
    print(pinaries[-1])