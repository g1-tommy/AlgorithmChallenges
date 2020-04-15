# 10988 팰린드롬인지 확인하기
if __name__ == "__main__":
    word = input()
    if len(word) % 2 == 0:
        left, right = word[:len(word) // 2], word[len(word) // 2:]
    else:
        left, right = word[:len(word) // 2], word[len(word) // 2 + 1:]
    if left == right[-1::-1]:
        print(1)
    else:
        print(0)