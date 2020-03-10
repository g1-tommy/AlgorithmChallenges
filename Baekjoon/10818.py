# 10818 최소, 최대
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0], arr[-1])