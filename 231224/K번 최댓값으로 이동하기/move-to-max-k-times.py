import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1

dxs, dys = [0,0,1,-1], [1,-1,0,0]
def possible(r, c):
    # 갈 수 있는 애들의 위치를 넣고 정렬
    target = arr[r][c]
    que = deque([(r, c)])
    result = []
    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True
    max_value = 0
    
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y + dys[k]
            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            if not visited[nx][ny] and arr[nx][ny] < target:
                que.append((nx,ny))
                visited[nx][ny] = True
                if max_value <= arr[nx][ny]:
                    max_value = arr[nx][ny]
                    result.append((nx, ny, arr[nx][ny]))
    result.sort(key = lambda x:(-x[2], x[0], x[1]))            
    return result

for _ in range(k):
    result = possible(sr,sc)
    if result :
        sr, sc, value = result[0]

    else:
        break
print(sr+1, sc+1)