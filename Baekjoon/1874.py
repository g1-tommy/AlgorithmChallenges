# 1874 스택 수열
if __name__ == "__main__":
    uList = list()
    stack = list()
    how = list()
    N = int(input())
    for _ in range(N):
        uList.append(int(input()))
    cursor = 1
    while len(uList) > 0:
        if len(stack) > 0 and stack[-1] == uList[0]:
            stack.pop()
            del uList[0]
            how.append('-')
        else:
            stack.append(cursor)
            if cursor > N:
                break
            cursor += 1
            how.append('+')
    if len(stack) > 0:
        print("NO")
    else:
        for _ in how:
            print(_)