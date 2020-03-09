# 5543 상근날드
if __name__ == "__main__":
    hamburgers = []
    drink = []
    for i in range(3):
        hamburgers.append(int(input()))
    for i in range(2):
        drink.append(int(input()))
    hamburgers.sort()
    drink.sort()
    print(hamburgers[0] + drink[0] - 50)