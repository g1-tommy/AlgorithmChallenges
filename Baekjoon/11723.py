# 11723 집합
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    M = int(input())
    cSet = list()
    for _ in range(M):
        uInput = input()
        try:
            command, arg = uInput.split()
            arg = int(arg)
        except:
            command = uInput
        
        if command == 'add':
            if not arg in cSet:
                cSet.append(arg)
        elif command == 'check':
            print(1 if arg in cSet else 0)
        elif command == 'remove':
            if arg in cSet:
                cSet.remove(arg)
        elif command == 'toggle':
            if arg in cSet:
                cSet.remove(arg)
            else:
                cSet.append(arg)
        elif command == 'all':
            cSet = [el for el in range(1, 21)]
        elif command == 'empty':
            cSet = list()