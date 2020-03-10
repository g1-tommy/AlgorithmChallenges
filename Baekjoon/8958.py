# 8958 OX퀴즈
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        score = 0
        previous = None
        conseq = 1
        for prob in list(input()):
            if prob == 'O':
                if previous != None:
                    if prob == previous:
                        conseq += 1
                        score += conseq
                    else:
                        score += 1
                else:
                    score += 1
                previous = 'O'
            else:
                previous = 'X'
                conseq = 1
        print(score)
