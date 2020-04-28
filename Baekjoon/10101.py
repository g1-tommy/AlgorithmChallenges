# 10101 삼각형 외우기
if __name__ == "__main__":
    angles = list()
    tot = 0
    for _ in range(3):
        tmp = int(input())
        angles.append(tmp)
        tot += tmp
    if angles == [60, 60, 60]:
        print("Equilateral")
    else:
        if tot == 180:
            if len(set(angles)) == 2:
                print("Isosceles")
            elif len(set(angles)) == 3:
                print("Scalene")
        else:
            print("Error")