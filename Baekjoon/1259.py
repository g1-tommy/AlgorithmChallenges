# 1259 팰린드롬 수
if __name__ == "__main__":
    cases = list()
    while True:
        case = int(input())
        if case == 0:
            break
        cases.append(case)

    for number in cases:
        number = str(number)
        left = number[:len(number) // 2]
        if len(number) % 2 == 0:
            right = number[len(number) // 2:]
        else:
            right = number[len(number) // 2 + 1:]
        if left == right[-1::-1]:
            print('yes')
        else:
            print('no')