import sys
input = sys.stdin.readline 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[sys.maxsize]*n for _ in range(n)]
dp[0][n-1] = arr[0][n-1]

for i in range(n):
    for j in range(n-1, -1, -1):
        if (i, j) == (0, n-1): continue
        if i == 0:
            dp[i][j] = dp[0][j+1] + arr[i][j]
        elif j == n-1:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = min(dp[i][j+1]+arr[i][j], dp[i-1][j]+arr[i][j])

print(dp[n-1][0])