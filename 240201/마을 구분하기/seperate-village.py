import sys
input = sys.stdin.readline 

PERSON = 1
WALL = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
town_cnt = 0
town_people_cnt = [] # 오름차순 
visited = [[False]*n for _ in range(n)]
tmp_cnt = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global tmp_cnt 
    dxs, dys = [0,0,1,-1],[1,-1,0,0]
    visited[x][y] = True

    for k in range(4):
        nx, ny =  x + dxs[k], y + dys[k]
        if not in_range(nx, ny):
            continue
        if not visited[nx][ny] and arr[nx][ny] == PERSON:
            visited[nx][ny] = True
            tmp_cnt += 1
            dfs(nx, ny)
    return 
            

            

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == PERSON:
            town_cnt += 1
            tmp_cnt = 1
            dfs(i,j)
            town_people_cnt.append(tmp_cnt)

print(town_cnt)
town_people_cnt.sort()
for ele in town_people_cnt:
    print(ele)