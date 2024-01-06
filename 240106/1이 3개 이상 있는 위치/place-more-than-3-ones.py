import sys
input =sys.stdin.readline


n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1, -1], [1,-1, 0, 0]
answer = 0
m = len(arr[0])

def dfs(x, y):
    cnt = 0
    global answer
    for k in range(4):
        nx, ny = x+dxs[k], y +dys[k]
        if nx < 0 or n <= nx or ny < 0 or m <= ny:
            continue
        if arr[nx][ny] == 1:
            cnt += 1
    if cnt >= 3:
        answer += 1

for i in range(n):
    for j in range(m):
        dfs(i, j)
            



print(answer)