import sys
input = sys.stdin.readline 
from collections import deque

n, m, fuel = map(int, input().split())
# (거리, 승객x, 승객y)
arr = [list(map(int, input().split())) for _ in range(n)]
cx, cy = map(int, input().split())
cx -= 1
cy -= 1
passengers = []
arrived = [False]*m
for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    passengers.append((sx-1, sy-1, ex-1, ey-1))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(idx, target_x, target_y):
    dxs, dys = [0,0, 1, -1], [1, -1, 0, 0]
    visited = [[-1]*n for _ in range(n)]
    que = deque()
    que.append((cx, cy))
    visited[cx][cy] = 0

    while que:
        x, y = que.popleft()
        if x == target_x and y == target_y:
            return (visited[x][y], target_x, target_y, idx)
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if visited[nx][ny] == -1 and arr[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    


def get_closest_passenger():
    result = []
    for idx in range(m):
        if not arrived[idx]:
            sx, sy, _, _ = passengers[idx]
            result.append(bfs(idx, sx, sy))
    result.sort(key = lambda x:(x[0], x[1], x[2]))
    # print(result[0][-1])
    return result[0]

def move2passenger(passenger):
    global fuel, cx, cy
    dist, x, y, idx = passenger
    
    # move
    cx, cy = x, y
    # fuel
    fuel -= dist
    return fuel <= 0

def move2goal_fill(passenger):
    global fuel, cx, cy
    _, _, _, idx = passenger
    dist, ex, ey, idx = bfs(idx, passengers[idx][2], passengers[idx][3])
    # move
    cx, cy = ex, ey
    arrived[idx] = True

    # fuel
    fuel -= dist
    if fuel < 0: return False
    fuel += (dist*2)
    return True



while True:
    if all(arrived) or fuel <= 0: break
    closest_passenger = get_closest_passenger()
    # print(closest_passenger)
    if move2passenger(closest_passenger): break
    if move2goal_fill(closest_passenger) == False:
        break

if fuel >= 0:
    print(fuel)
else:
    print(-1)