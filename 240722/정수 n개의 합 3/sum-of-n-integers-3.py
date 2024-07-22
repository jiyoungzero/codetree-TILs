import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = -1
prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    prefix[1][i+1] = arr[0][i]
    prefix[i+1][1] = arr[i][0]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]



for i in range(n-k+1):
    for j in range(n-k+1):
        sx, sy = i, j
        ex, ey = i+k, j+k
        answer = max(answer, prefix[ex][ey] - prefix[sx][ey] - prefix[ex][sy] + prefix[sx][sy])
print(answer)