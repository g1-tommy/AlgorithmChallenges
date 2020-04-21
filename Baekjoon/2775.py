# 2775 부녀회장이 될테야
"""
풀이: DP 이용
"""
if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        residents = [el for el in range(1, n + 1)]
        for i in range(k):
            for j in range(1, n):
                residents[j] += residents[j-1]
        print(residents[n-1])