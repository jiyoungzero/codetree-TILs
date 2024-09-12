import sys
input = sys.stdin.readline
from collections import deque

WALL = -1
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
stores = {} # 인덱스가 해당 사람이 가고 싶은 편의점을 나타냄 
for idx in range(1, m+1):
    x, y = map(int, input().split())
    stores[idx] = [x-1, y-1]
answer = 0
ppl = {}
arrived = [False]*(m+1)
arrived[0] = True 
times = 1
ppl2path = {}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def bfs(sx, sy, goal):
    que = deque()
    que.append((sx, sy, []))    
    
    visited = [[False]*n for _ in range(n)]
    result = []
    visited[sx][sy] = True

    while que:
        x, y, path = que.popleft()
        if [x, y] == goal: 
            result = path
            break

        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue 

            if arr[nx][ny] != WALL and not visited[nx][ny]:
                # path.append((nx, ny))
                visited[nx][ny] = True
                que.append((nx, ny, path + [(nx, ny)]))
    return result[::-1]
    
    

def move_to_stores(idx):
    x, y = ppl[idx]

    path = bfs(x, y, stores[idx])
    ppl2path[idx] = path
    now_path = ppl2path[idx]

    # 한 칸 이동 
    nx, ny = now_path.pop()
    ppl[idx] = [nx, ny]
    if [nx, ny] == stores[idx]:
        arrived[idx] = True 



def move_to_basecamp(idx):
    sx, sy = stores[idx]
    que = deque()
    que.append((sx, sy))
    visited = [[-1]*n for _ in range(n)]
    visited[sx][sy] = 0

    basecamps = [] # (거리, 행, 열 )
 
    while que:
        x, y = que.popleft()
            
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue
            if arr[nx][ny] != WALL and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                if arr[nx][ny] == 1:
                    basecamps.append((visited[nx][ny], nx, ny))
    
    basecamps.sort(key = lambda x : (x[0], x[1], x[2]))
    closest_bc = [basecamps[0][1], basecamps[0][2]]
    
    # 해당 베이스 캠프로 이동
    ppl[idx] = closest_bc
    arr[closest_bc[0]][closest_bc[1]] = WALL


while not all(arrived):

    for k, v in ppl.items():
        if arrived[k] : continue
        move_to_stores(k)

    # 편의점에 도착한 사람은 해당 칸 더이상 못 지나감
    for idx in range(1, m+1):
        if arrived[idx]:
            x, y = stores[idx]
            arr[x][y] = WALL

    if times <= m:
        move_to_basecamp(times)
    answer += 1
    times += 1

print(answer)