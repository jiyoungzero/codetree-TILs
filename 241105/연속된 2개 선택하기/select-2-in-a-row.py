n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = arr[1]
dp[2] = dp[1] + arr[2]


for i in range(3, n+1):
    # print(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])

print(dp[-1])