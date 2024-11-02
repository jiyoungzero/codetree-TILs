n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        cur = arr[i][j]
        if i==n-1 and j == n-1:
            break
        # print(i+cur, j+cur)
        if i+cur < n and n <= j+cur :
            dp[i+cur][j] += dp[i][j]
        elif n <= i+cur and j+cur < n:
            dp[i][j+cur] += dp[i][j]
        elif i+cur < n and j+cur < n: 
            dp[i+cur][j] += dp[i][j]
            dp[i][j+cur] += dp[i][j]

print(dp[-1][-1])