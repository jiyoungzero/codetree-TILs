import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


dp = [0]*n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = dp[i-1]+arr[i]
dp = [0] + dp

# print(*dp)
for i in range(n+1):
    for j in range(i):
        if dp[i]-dp[j] == k:
            answer += 1
            # print(i, j) # 1 3 4 6
print(answer)