# 9012 괄호
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        error = False
        stack = list()
        for token in input():
            if token == '(':
                stack.append('(')
            elif token == ')':
                try:
                    stack.pop()
                except IndexError:
                    error = True
                    break
        if len(stack) == 0 and not error:
            print('YES')
        else:
            print('NO')