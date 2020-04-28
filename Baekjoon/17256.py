# 17256 달달함이 넘쳐흘러
if __name__ == "__main__":
    vars = list()
    for _ in range(2):
        vars.append(list(map(int, input().split())))
    print(vars[-1][0] - vars[0][-1], vars[-1][1] // vars[0][1], vars[-1][-1] - vars[0][0])