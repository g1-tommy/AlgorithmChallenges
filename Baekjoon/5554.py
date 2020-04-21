# 5554 심부름 가는 길
if __name__ == "__main__":
    sum = 0
    for _ in range(4):
        sum += int(input())
    
    print(sum // 60)
    print(sum % 60)