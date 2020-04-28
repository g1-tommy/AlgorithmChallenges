# 16428 A/B - 3
if __name__ == "__main__":
    A, B = map(int, input().split())
    if A == 0:
        print(0)
        print(0)
    else:
        print(A // B if B > 0 else A // B + 1)
        print(A % B if B > 0 else A % B + abs(B))