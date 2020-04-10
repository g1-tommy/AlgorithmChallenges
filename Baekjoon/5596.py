# 5596 시험 점수
if __name__ == "__main__":
    mingook = list(map(int, input().split()))
    manse = list(map(int, input().split()))
    S = 0
    T = 0
    for item in mingook:
        S += item
    for item in manse:
        T += item
    if S == T:
        print(S)
    elif S > T:
        print(S)
    else:
        print(T)