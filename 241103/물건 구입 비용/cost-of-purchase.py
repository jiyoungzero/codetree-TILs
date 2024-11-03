n, p = map(int, input().split())
stocks = [tuple(map(int, input().split())) for _ in range(p)]


dp = [int(1e9)]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(p):
        cnt, price = stocks[j]
        mul = 1
        while cnt * mul <= i:
            dp[i] = min(dp[i], dp[i-cnt*mul] + mul * price)
            mul += 1
print(dp[n])