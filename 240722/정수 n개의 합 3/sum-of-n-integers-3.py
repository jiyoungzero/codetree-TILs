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

def get_sum(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

for i in range(1, n-k+2):
    for j in range(1, n-k+2):
        answer = max(answer, get_sum(i, j, i+k-1, j+k-1))
print(answer)