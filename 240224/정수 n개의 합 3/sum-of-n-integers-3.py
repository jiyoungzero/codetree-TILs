import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = [[0]*(n+1)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append([0]+tmp)
prefix_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = arr[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]


answer = 0
for i in range(k, n+1-k):
    for j in range(k, n+1-k):
        tmp_sum = prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + arr[i-k][j-k]
        answer = max(answer, tmp_sum)
print(answer)