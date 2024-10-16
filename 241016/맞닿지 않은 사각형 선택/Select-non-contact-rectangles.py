n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]
dp = [[0]*n for _ in range(2)]

dp[0][0], dp[0][1] = arr[0][0], arr[0][1]
for j in range(1, n):
    dp[0][j] = max(dp[1][j-1] + arr[0][j], dp[0][j-1])
    dp[1][j] = max(dp[0][j-1] + arr[1][j], dp[1][j-1])
print(max(dp[0][-1], dp[1][-1]))