import sys
input = sys.stdin.readline 
from collections import deque

R, C, K = map(int, input().split())
arr = [[0]*C for _ in range(R+3)]
dxs, dys = [-1,0,1,0],[0,1,0,-1] # 위, 오른쪽, 아래, 왼쪽 
fairies = [tuple(map(int, input().split())) for _ in range(K)] # (출발열, 출구방향)
answer = 0 # 행의 누적합

l_check = [(-1, -1), (0, -2), (1, -1), (1,-2),(2,-1)]
r_check = [(-1, 1),(0,2),(1,1),(1,2),(2,1)]
d_check = [(1, -1), (2, 0), (1, 1)]
# 1) 골렘 이동 우선순위
# : 아래 -> 왼쪽 + 아래 (골렘 반시계방향으로 회전, 출구도 반시계 방향으로 회전) 
# : -> 오른쪽 + 아래 (골렘 시계방향으로 회전, 출구도 시계방향으로 회전)

# 2) 정령 아래로 이동 
# 가장 아래로 이동 (출구 + 다른 골렘 인접이라면, 다른 골렘 쪽으로 내려감)

# 3) 정령 위치 판단
# 3-1) 정령의 위치가 배열 밖이라면, arr 모두 비우기 -> 다음 골렘이 새롭게 탐색
# 3-2) 정령의 위치가 배열 안이라면 answer += 정령.행 

def in_range(x, y):
    return 0 <= x < R and 0 <= y < C

def is_fairy_out(x, y):
    return x < 3

def rotate_out(rotate, dir, x, y): # (왼쪽인지 오른쪽인지, 출구방향, 현재출구위치)
    if rotate == 'right': # 시계방향 회전
        if dir == 0:
            return (2, 2)
        elif dir == 1:
            return (2, 0)
        elif dir == 2:
            return (0, 0)
        else:
            return (0, 2)
    else: # 반시계방향 회전 
        if dir == 0:
            return (2, -2)
        elif dir == 1:
            return (0, -2)
        elif dir == 2:
            return (0, 0)
        else:
            return (2, 0)

# 왼쪽 + 아래로 갈 수 있는지
def can_go_left(sx, sy): # 요정의 위치
    for dx,dy in l_check:
        x, y = sx+dx, sy+dy
        if not in_range(x, y):
            return False
        if arr[x][y] != 0:
            return False
    return True

# 오른쪽 + 아래로 갈 수 있는지
def can_go_right(sx, sy):
    for dx,dy in r_check:
        x, y = sx+dx, sy+dy
        if not in_range(x, y):
            return False
        if arr[x][y] != 0:
            return False
    return True

def can_go_down(sx, sy):
    for dx,dy in d_check:
        x, y = sx+dx, sy+dy
        if not in_range(x, y):
            return False
        if arr[x][y] != 0:
            return False
    return True

def move_golam(f_idx):
    # 현재 정령의 정보
    x = 1
    y, out_dir = fairies[f_idx]
    ox, oy = x + dxs[out_dir], y + dys[out_dir]
    while True:
        if can_go_down(x, y):
            x += 1
            ox = ox + 1
        elif can_go_left(x, y):
            x += 1
            y -= 1
            r_dx, r_dy = rotate_out('left', out_dir, ox, oy) 
            ox, oy = ox + r_dx, oy + r_dy
            out_dir = (out_dir - 1)%4 ### !!!!!!!!!!! 이거 잘 되는지 확인하기
        elif can_go_right(x, y):
            x += 1
            y += 1
            r_dx, r_dy = rotate_out('right', out_dir, ox, oy)
            ox, oy = ox + r_dx, oy + r_dy
            out_dir = (out_dir+1)%4
        else:
            break
    return (x, y, ox, oy)

def move_fairy(fx, fy, ox, oy):
    que = deque()
    que.append((fx, fy))
    visited = [(fx, fy)]

    # 갔던 모든 곳들 중 x의 값이 가장 큰 곳
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx,ny):continue
            if arr[x][y] == -1 and arr[nx][ny] != 0: # 출구이므로 nx,ny가 0만 아니라면 이동가능
                que.append((nx, ny))
                visited.append((nx, ny))
            elif arr[nx][ny] == -1 or arr[x][y] == arr[nx][ny]:
                que.append((nx, ny))
                visited.append((nx,ny))

    visited.sort(key = lambda x:(-x[0]))
    return visited[0]

for f_idx in range(K):
    fx, fy, out_x, out_y = move_golam(f_idx)

    # 이동한 골렘 위치에 대한 arr 표시 (골렘 : f_idx + 1, 출구 : -1)
    arr[fx][fy] = f_idx + 1
    arr[out_x][out_y] = -1
    for dir in range(4):
        n_fx, n_fy = fx + dxs[dir], fy + dys[dir]
        if (n_fx, n_fy) != (out_x, out_y):
            arr[n_fx][n_fy] = f_idx + 1
        
    fx, fy = move_fairy(fx, fy, out_x, out_y)
    
    if is_fairy_out(fx, fy):
        arr = [[0]*C for _ in range(R+3)]
    
    else: answer += fx
print(answer)