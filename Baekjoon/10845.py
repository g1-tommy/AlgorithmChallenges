# 10845 큐
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    queue = list()
    N = int(input())
    for i in range(N):
        uInput = input().split()
        if len(uInput) > 1:
            command, arg = uInput
        else:
            command = uInput[0]
        
        if command == 'push':
            queue.append(int(arg))
        elif command == 'pop':
            try:
                print(queue[0])
                queue.remove(queue[0])
            except IndexError:
                print(-1)
        elif command == 'front':
            if len(queue) > 0:
                print(queue[0])
            else:
                print(-1)
        elif command == 'back':
            if len(queue) > 0:
                print(queue[-1])
            else:
                print(-1)
        elif command == 'empty':
            print(1 if len(queue) == 0 else 0)
        elif command == 'size':
            print(len(queue))