# 1193 분수찾기
"""
풀이: Table을 다이아몬드 형태로 돌려서 패턴 추출
"""
if __name__ == "__main__":
    X = int(input())
    tmp = 1
    sum = 0
    while sum + tmp < X:
        sum += tmp
        tmp += 1
    if tmp % 2 == 0: # Right Direction
        print(f"{1 + ((X - sum) - 1)}/{tmp - ((X - sum) - 1)}")
    else:            # Left Direction
        print(f"{tmp - ((X - sum) - 1)}/{1 + ((X - sum) - 1)}")
