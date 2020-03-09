# 10952 A+B - 5
if __name__ == "__main__":
    while True:
        data = input()
        if data == '0 0':
            break
        a, b = map(int, data.split())
        print(a + b)