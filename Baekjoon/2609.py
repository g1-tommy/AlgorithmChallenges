# 2609 최대공약수와 최소공배수
if __name__ == "__main__":
    A, B = map(int, input().split())
    mul = A * B
    temp = A % B
    while temp != 0:
        temp = A % B
        A = B
        B = temp
    print(A) # GCD
    print(mul // A)