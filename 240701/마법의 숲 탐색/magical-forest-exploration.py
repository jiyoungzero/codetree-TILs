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


def in_range(x, y):
    return 0 <= x < R+3 and 0 <= y < C

def is_galam_out(x, y):
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
    y -= 1
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


def move_fairy(f_idx, fx, fy, ox, oy):
    que = deque()
    que.append((fx, fy))
    que.append((ox, oy))
    visited = [(fx, fy), (ox, oy)]

    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx,ny):continue
            if (nx, ny) not in visited:
                if arr[x][y] < 0 and arr[nx][ny] != 0: # 현재 출구일 경우
                    que.append((nx, ny))
                    visited.append((nx, ny))
                elif (arr[x][y] == abs(arr[nx][ny])): # 출구는 아니지만 같은 골렘인 경우
                    que.append((nx,ny))
                    visited.append((nx, ny))

    # print('visited = ', visited)    
    visited.sort(key = lambda x:(-x[0]))
    
    return visited[0]

for f_idx in range(K):
    fx, fy, out_x, out_y = move_golam(f_idx)

    if is_galam_out(fx-1, fy):
        arr = [[0]*C for _ in range(R+3)]
        continue

    # 이동한 골렘 위치에 대한 arr 표시 (골렘 : f_idx + 1, 출구 : -(f_idx + 1))
    arr[fx][fy] = f_idx + 1
    arr[out_x][out_y] = -(f_idx+1)
    for dir in range(4):
        n_fx, n_fy = fx + dxs[dir], fy + dys[dir]
        if not in_range(n_fx, n_fy):continue
        if (n_fx, n_fy) != (out_x, out_y):
            arr[n_fx][n_fy] = f_idx + 1
        
    fx, fy = move_fairy(f_idx, fx, fy, out_x, out_y)

    # print(f_idx+1, '-> 행번호', fx-2)
    # for row in arr[3:]:
    #     print(*row)
    answer += (fx-2)
print(answer)