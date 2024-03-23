n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
dp = [0]*(n+1)
dp[1] = arr[0]%7

for i in range(2, n+1):
    dp[i] = (arr[i-1]%7+dp[i-1])%7

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if dp[j] == dp[i-1]:
            answer = max(answer, j-i+1)

print(answer)