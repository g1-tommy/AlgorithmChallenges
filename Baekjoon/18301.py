# 18301 Rats
if __name__ == "__main__":
    N1, N2, N12 = map(int, input().split())
    print((N1 + 1) * (N2 + 1) // (N12 + 1) - 1)