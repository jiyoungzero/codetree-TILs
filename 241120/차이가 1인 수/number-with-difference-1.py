MOD = 10**9 + 7
n = int(input())

# dp[i][j] : i자리 수에서 끝자리가 j인 경우의 수
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j != 0:
            dp[i][j] += dp[i-1][j-1]
        if j != 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= MOD

answer = 0
for i in range(10):
    answer += dp[n][i]
print(answer%MOD)
