n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
dp = [0]*(n+1)
dp[1] = arr[0]

for i in range(2, n+1):
    dp[i] = arr[i-1]+dp[i-1]

for a in range(1, n+1):
    for b in range(a+1, n+1):
        if (dp[b]-dp[a-1])%7 == 0:
            answer = max(answer, b-a+1)
print(answer)