import sys
input = sys.stdin.readline 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0]*(1+n) for _ in range(n+1)]

prefix[0][0] = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]



def get_sum(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1] 

answer = -int(1e9)
for sr in range(1, n+1):
    for er in range(sr, n+1):
        dp = [0]*(n+1) 
        for y in range(1, n+1):
            v = get_sum(sr, y, er, y)
            dp[y] = max(dp[y-1]+v, v)

        answer = max(answer, max(dp[1:]))
print(answer)