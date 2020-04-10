# 1085 직사각형에서 탈출
if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    minX = w
    minY = h
    vertical = h - y
    horizontal = w - x
    if horizontal > vertical:
        if minY > vertical:
            minY = vertical
    elif vertical > horizontal:
        if minX > horizontal:
            minX = horizontal
    if x > w - x:
        if minX > w - x:
            minX = w - x
    else:
        if minX > x:
            minX = x
    if h - y > y:
        if minY > y:
            minY = y
    else:
        if minY > h - y:
            minY = h - y
    if minX > minY:
        print(minY)
    else:
        print(minX)
        