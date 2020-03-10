# 2577 숫자의 개수
if __name__ == "__main__":
    arr = [0,0,0,0,0,0,0,0,0,0]
    mul = 1
    for i in range(3):
        mul *= int(input())
    
    while mul != 0:
        arr[mul % 10] += 1
        mul //= 10
    
    for i in arr:
        print(i)