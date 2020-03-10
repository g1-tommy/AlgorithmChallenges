# 1157 단어공부
if __name__ == "__main__":
    arr = [0 for i in range(26)]
    string = input().lower()
    for i in string:
        arr[(ord(i) - 97)] += 1
    maxCount = max(arr)
    maxStr = chr(arr.index(maxCount) + 97)
    arr.sort()
    if (arr[-1] == arr[-2]):
        print('?')
    else:
        print(maxStr.upper())
    