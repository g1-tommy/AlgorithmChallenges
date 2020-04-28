# 2579 계단 오르기
"""
풀이 : DP 이용
"""
if __name__ == "__main__":
    N = int(input())
    floorScores = list()
    dp = [0] * 300
    for _ in range(N):
        floorScores.append(int(input()))
    dp[0] = floorScores[0]
    if N > 1:
        dp[1] = max(floorScores[0] + floorScores[1], floorScores[1])
    if N > 2:
        dp[2] = max(floorScores[0] + floorScores[2], floorScores[1] + floorScores[2])
    for _ in range(3, N):
        dp[_] = max(dp[_ - 2] + floorScores[_], dp[_ - 3] + floorScores[_ - 1] + floorScores[_])
    print(dp[N - 1])