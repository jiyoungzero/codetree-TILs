import sys
input = sys.stdin.readline 
from collections import deque


k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
fragments = deque(map(int, input().split()))
answer = []
path = []

dxs, dys = [0,0,1,-1],[1,-1,0,0]
def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5 

def deepcopy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def get_values(a):
    global path
    visited = [[False]*5 for _ in range(5)]
    result = 0
    path = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                p, visit = bfs(i, j, visited, a)
                visited = visit[:]
                if len(p) >= 3:
                    result += len(p)
                    path += p
    return result
                
def bfs(sx, sy, visited, a):
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True 
    path = [(sx, sy)]
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue
            if not visited[nx][ny] and a[sx][sy] == a[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny)) 
                path.append((nx, ny))
    return (path, visited)
    
    
def rotate_90(a, sr, sc):
    r_a = deepcopy(a)
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            oi, oj = i-sr, j-sc
            ri, rj = oj, 3 - oi - 1
            fi, fj = ri + sr, rj + sc
            r_a[fi][fj] = a[i][j]
    return r_a


def find_max_part(): # sx, sy, r_cnt return 
    global test_visited

    lst = [] # (1차 획득, 각도, 열, 행)
    for r_cnt in range(1, 4):
        for col in range(3):
            for row in range(3):
                test_arr = deepcopy(arr)
                # r_cnt만큼 회전시키기
                for _ in range(r_cnt):
                    test_arr = rotate_90(test_arr, row, col)
                # 1차 획득 가치 구하기
                lst.append((get_values(test_arr), r_cnt, col+1, row+1))
    lst.sort(key = lambda x: (-x[0], x[1], x[2], x[3]))
    find = (lst[0][3]-1, lst[0][2]-1, lst[0][1], lst[0][0])
    return find # sx, sy, r_cnt    

def fill_frags(cnt):
    global arr, path, fragments, answer
    cnt += len(path)
    path.sort(key = lambda x:(x[1], -x[0]))
    for x, y in path:
        arr[x][y] = fragments.popleft()
    return cnt

for _ in range(k):
    sx, sy, r_cnt, values = find_max_part()
    if values == 0:
        break
    for _ in range(r_cnt):
        arr = rotate_90(arr, sx, sy)
    cnt = 0
    while True:
        if get_values(arr) > 0:
            cnt = fill_frags(cnt)
        else:
            break
        
    if cnt: answer.append(cnt)
print(*answer)