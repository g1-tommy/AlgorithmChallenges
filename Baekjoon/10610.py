# 10610 30
if __name__ == "__main__":
    N = list(map(int, input()))
    if sum(N) % 3 == 0 and 0 in N:
        N.pop(N.index(0))
        N = list(reversed(sorted(N)))
        N.append(0)
        print("".join(map(str, N)))
    else:
        print(-1)