import sys
input = sys.stdin.readline


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dxs, dys = [0,0,1,-1],[1,-1,0,0]
answer = [] # 각 마을의 주민 수 

def dfs(x, y):
    global cnt
    for k in range(4):
        nx, ny = x+dxs[k], y + dys[k]
        if nx < 0 or ny < 0 or n <= nx or n <= ny:continue
        elif visited[nx][ny] : continue
        elif maps[nx][ny] == 1:
            visited[nx][ny] = True
            cnt += 1
            dfs(nx, ny)



for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            visited[i][j] = True
            cnt = 1
            dfs(i,j)
            answer.append(cnt)
answer.sort()
print(len(answer))
for ele in answer:
    print(ele)