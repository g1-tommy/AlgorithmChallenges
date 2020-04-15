# 10866 덱
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    deque = list()
    N = int(input())
    for i in range(N):
        uInput = input().split()
        if len(uInput) > 1:
            command, arg = uInput
        else:
            command = uInput[0]

        if command == 'push_front':
            deque = [int(arg)] + deque
        elif command == 'push_back':
            deque.append(int(arg))
        elif command == 'pop_front':
            if len(deque) > 0:
                print(deque[0])
                deque.pop(0)
            else:
                print(-1)
        elif command == 'pop_back':
            if len(deque) > 0:
                print(deque[-1])
                deque.pop()
            else:
                print(-1)
        elif command == 'size':
            print(len(deque))
        elif command == 'empty':
            print(0 if len(deque) > 0 else 1)
        elif command == 'front':
            if len(deque) > 0:
                print(deque[0])
            else:
                print(-1)
        elif command == 'back':
            if len(deque) > 0:
                print(deque[-1])
            else:
                print(-1)