# 1855 암호
if __name__ == "__main__":
    K = int(input())
    cursor = 0
    tmpLst = list()
    compareLst = list()
    u = list(input())
    rows = len(u) // K
    reverse = False
    for _ in u:
        tmpLst.append(_)
        cursor += 1
        if cursor % K == 0:
            if not reverse and cursor % (2*K) == 0:
                reverse = True
            else:
                reverse = False
            if reverse:
                tmpLst.reverse()
            compareLst.append(tmpLst)
            tmpLst = list()
    compareLst.append(tmpLst)
    newStr = ''
    for i in range(K):
        for j in range(rows):
            newStr += compareLst[j][i]
    print(newStr)