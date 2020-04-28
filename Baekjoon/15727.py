# 15727 조별과제를 하려는데 조장이 사라졌다
if __name__ == "__main__":
    dist = int(input())
    cursor = 5
    count = 0
    while dist > 0:
        if dist - cursor < 0:
            cursor -= 1
            continue
        else:
            dist -= cursor
            count += 1
    print(count)