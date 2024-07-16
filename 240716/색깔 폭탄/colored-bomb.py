import sys
input = sys.stdin.readline 
from collections import deque

ROCK = -1
RED = 0
BLANK = -2

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bombs = [] 
visited = [[False]*n for _ in range(n)]
answer = 0
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def deepcopy(a):
    return [
        a[row][:]
        for row in range(len(a))
    ]
    
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy, target): # [크기, 빨간색 개수, 기준점 x, 기준점 y, [pos]]
    global visited
    que  = deque()
    que.append((sx, sy))
    visited[sx][sy] = True

    pos = [(sx, sy)]
    result = [1, 0, sx, sy, pos]
    if arr[sx][sy] == RED:
        result[1] += 1
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and (arr[nx][ny] == target or arr[nx][ny] == RED):
                if nx > result[2]:
                    result[2],result[3] = nx, ny
                elif nx == result[2] and ny < result[3]:
                    result[2],result[3] = nx, ny

                visited[nx][ny] = True
                if arr[nx][ny] == RED:
                    result[1] += 1
                result[0] += 1
                pos.append((nx, ny))
                que.append((nx, ny))
    for i in range(n):
        for j in range(n):
            if arr[i][j] == RED:visited[i][j] = False
    if result[0] >= 2 and result[0] != result[1]: return result
    else: return False

def find_all_bombs():
    global bombs
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                bomb = bfs(i, j, arr[i][j])
                if bomb != False:
                    bombs.append(bomb)
                    
def find_largest_bomb():
    bombs.sort(key = lambda x:(-x[0], x[1], -x[2], x[3]))
    return bombs[0] 

def del_bomb(bomb):
    global arr, answer
    for x, y in bomb[4]:
        arr[x][y] = BLANK
    C = len(bomb[4])
    answer += (C*C)


def gravity():
    global arr
    nxt_arr = [[BLANK]*n for _ in range(n)]

    for col in range(n):
        now = n-1
        for row in range(n-1, -1, -1):
            if arr[row][col] == ROCK:
                nxt_arr[row][col] = ROCK
                now = row - 1
            elif arr[row][col] == BLANK:
                continue
            else:
                nxt_arr[now][col] = arr[row][col]
                now -= 1
    arr = deepcopy(nxt_arr)


def rotate_90(): # 3번 회전시키기 (반시계)
    global arr
    nxt_arr = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            nxt_arr[j][n-i-1] = arr[i][j]

    arr = deepcopy(nxt_arr)    


while True:
    visited = [[False]*n for _ in range(n)]
    bombs = [] 

    find_all_bombs()
    if not bombs: break
    # print(bombs)
    del_bomb(find_largest_bomb())
    gravity()
    for _ in range(3):
        rotate_90()
    gravity()

print(answer)

# for row in arr:
#     print(*row)
# print()
# rotate_90()

# for row in arr:
#     print(*row)