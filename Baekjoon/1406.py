# 1406 에디터
"""
Hint: Stack 사용
Time Complexity를 위해 두 개의 Stack List 활용
"""
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    stack1 = list(input().strip())
    stack2 = list()
    N = int(input())
    for _ in range(N):
        line = input().strip()
        if line[0] == 'L':
            if stack1:
                stack2.append(stack1.pop())
        elif line[0] == 'D':
            if stack2:
                stack1.append(stack2.pop())
        elif line[0] == 'B':
            if stack1:
                stack1.pop()
        elif line[0] == 'P':
            stack1.append(line[-1])
    print(''.join(stack1 + list(reversed(stack2))))