# 1360 되돌리기
"""
풀이:
Commands를 스택 형태로 전부 저장 후, 하나씩 pop하여
pop한 command의 timestamp - duration초에 실행한만큼의 command를 pop한다.
"""
if __name__ == "__main__":
    N = int(input())
    commStack = list()
    tmpStack = list()
    for i in range(N):
        command, arg, timestamp = map(str, input().split())
        commStack.append(dict(command=command, arg=arg, timestamp=int(timestamp)))

    while len(commStack) > 0:
        lastCommand = commStack.pop()
        if lastCommand["command"] == "undo":
            while len(commStack) > 0 and commStack[-1]["timestamp"] >= lastCommand["timestamp"] - int(lastCommand["arg"]):
                commStack.pop()
        elif lastCommand["command"] == "type":
            tmpStack = [lastCommand["arg"]] + tmpStack
    
    print("".join(tmpStack))