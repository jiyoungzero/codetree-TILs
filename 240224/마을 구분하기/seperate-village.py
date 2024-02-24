import sys
input = sys.stdin.readline 


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
cnt_lst = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global cnt
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    for k in range(4):
        nx, ny = x + dxs[k], y+dys[k]
        if not in_range(nx, ny):
            continue
        if arr[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            cnt += 1
            dfs(nx, ny)
    

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            dfs(i, j)
            cnt_lst.append(cnt)

cnt_lst.sort()
print(len(cnt_lst))
for ele in cnt_lst:
    print(ele)