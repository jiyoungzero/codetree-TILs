import sys
input = sys.stdin.readline 

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 2
if n == 1:
    print(2)
else:
    dp[2] = 7
    for i in range(3, n+1):
        dp[i] = ((dp[i-1]*2)+ (dp[i-2] * 3) + (dp[i-3]*2))%1000000007
    print(dp[n])