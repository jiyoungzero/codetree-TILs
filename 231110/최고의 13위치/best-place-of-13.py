import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n-2):
        answer = max(answer,  arr[i][j]+arr[i][j+1]+arr[i][j+2])
print(answer)