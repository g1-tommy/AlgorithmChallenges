# 2908 상수
if __name__ == "__main__":
    A, B = input().split()
    A = int(A[::-1])
    B = int(B[::-1])
    if A > B:
        print(A)
    elif A < B:
        print(B)
    