import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = -int(1e9)
for length in range(k, n+1):
    dp = [-int(1e9)]*n
    dp[0] = sum(arr[:length])
    for i in range(length, n):
        dp[i] = dp[i-1] - arr[i-length] + arr[i]
    answer = max(answer, max(dp))
        
print(answer)