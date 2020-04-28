# 15873 공백 없는 A + B
if __name__ == "__main__":
    Ns = list(reversed(list(map(int, input()))))
    A = 0
    B = 0
    if 0 in Ns:
        cursor = 0
        turnA = False
        for idx, item in enumerate(Ns):
            if not turnA:
                if idx != 0 and item == 0:
                    turnA = True
                    cursor = 1
                    continue
                else:
                    B += (10 ** cursor) * item
                    if B == 10:
                        turnA = True
                        cursor = 0
                        continue
            else:
                A += (10 ** cursor) * item
            cursor += 1
    else:
        B, A = Ns[0], Ns[-1]
    print(A + B)