n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
dp = [0]*(n+1)
dp[1] = arr[0]%7
mod = [[int(1e9), 0] for _ in range(7)]
mod[dp[1]%7] = [0, 0]

for i in range(1, n):
    dp[i+1] = arr[i] + dp[i]
    tmp = dp[i+1]%7
    if mod[tmp][0] > i:
        mod[tmp][0] = i 
    if mod[tmp][1] < i:
        mod[tmp][1] = i
    
for a, b, in mod:
    if abs(a-b) != int(1e9):
        answer = max(answer, abs(a-b))
print(answer)