# 10809 알파벳 찾기
if __name__ == "__main__":
    arr = [-1 for i in range(26)]
    inputStr =  input()
    for idx, i in enumerate(inputStr):
        if arr[(ord(i) - 96) - 1] == -1:
            arr[(ord(i) - 96) - 1] = idx
    print(" ".join(map(str, arr)))