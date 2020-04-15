# 10828 스택
import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    stack = list()
    for i in range(N):
        uInput = sys.stdin.readline().split()
        if len(uInput) > 1:
            command, arg = uInput
        else:
            command = uInput[0]
        if command == 'push':
            stack.append(int(arg))
        elif command == 'pop':
            try:
                print(stack[-1])
                stack.pop()
            except IndexError:
                print(-1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            print(1 if len(stack) == 0 else 0)
        elif command == 'top':
            print(stack[-1] if len(stack) > 0 else -1)
