import sys
input = sys.stdin.readline 
from collections import deque

BLANK = 0
WALL = 2
TRAP = 1

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

dxs, dys = [-1,0,1,0],[0,1,0,-1] # 상 우 하 좌 
L, N, Q = map(int, input().split())
chase = [list(map(int, input().split())) for _ in range(L)]
original_chase = deep_copy(chase)

knights = {}
for idx in range(3, N+3):
    r, c, h, w, k = list(map(int, input().split()))
    knights[idx] = [r-1, c-1, h, w, k]
    for row in range(r-1, r-1+h):
        for col in range(c-1, c-1+w):
            chase[row][col] = idx
cmds = [tuple(map(int, input().split())) for _ in range(Q)] # 왕의 명령
dead = [False]*(N+3)
sum_damage = [0]*(N+3)

# print('*chase')
# for row in chase:
#     print(*row)
# print()

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L

def bfs(idx, dir):
    que = deque()
    visited = [[False]*L for _ in range(L)]

    x, y = knights[idx][0], knights[idx][1]
    for row in range(x, x + knights[idx][2]):
        for col in range(y, y + knights[idx][3]):
            que.append((row, col))
            visited[row][col] = True

    push_set = set()
    while que:
        x, y = que.popleft()
        nx, ny = x + dxs[dir], y + dys[dir]
        if not in_range(nx, ny):
            return -1
        if original_chase[nx][ny] == WALL:
            return -1 
        if not visited[nx][ny] and (chase[nx][ny] >= 3 and chase[nx][ny] != idx):
            push_set.add(chase[nx][ny])
            visited[nx][ny] = True 
            que.append((nx, ny))
    return push_set


def move_knights(idx, dir):
    global chase 

    if dead[idx]:return
    # idx번째 기사와 맞닿아있는 기사의 pos를 담은 lst반환 
    push_set = bfs(idx, dir)
    if push_set == -1:return 

    que = deque()
    for ele in list(push_set):
        que.append(ele)
    while que:
        cur = que.popleft()
        tmp = bfs(cur, dir)
        if tmp == -1:return
        else:
            push_set.update(tmp)
            for ele in list(tmp):
                que.append(ele)
    
    # 각각 한 칸씩 움직임 처리
    push_set.add(idx)
    nxt_chase = deep_copy(chase)
    # print(push_set)
    for k_idx in list(push_set):
        x, y = knights[k_idx][0], knights[k_idx][1]
        h, w = knights[k_idx][2], knights[k_idx][3]
        for r in range(x, x+h):
            for c in range(y, y+w):
                nxt_chase[r][c] = BLANK

    for k_idx in list(push_set):
        x, y = knights[k_idx][0], knights[k_idx][1]
        h, w = knights[k_idx][2], knights[k_idx][3]
        for r in range(x, x+h):
            for c in range(y, y+w):         
                nxt_chase[r+dxs[dir]][c+dys[dir]] = k_idx

    for k_idx in list(push_set):
        knights[k_idx][0] += dxs[dir]
        knights[k_idx][1] += dys[dir]
    
    # print('*nxt_chase')
    # for row in nxt_chase:
    #     print(*row)

    # 데미지 계산 
    # print("idx: ", idx, push_set, " push_set")
    for k_idx in list(push_set):
        if k_idx == idx or dead[k_idx]:continue 
        # print("k_idx =", k_idx, 'pushing')
        x, y = knights[k_idx][0], knights[k_idx][1]
        h, w = knights[k_idx][2], knights[k_idx][3] 
        damage = 0
        for r in range(x, x + h):
            for c in range(y, y + w):
                if original_chase[r][c] == TRAP:
                    damage += 1
        # print(k_idx, "이동 시 데미지 :", damage, (x, y), (x+h, y+w))
        knights[k_idx][-1] -= damage
        sum_damage[k_idx] += damage
        if knights[k_idx][-1] <= 0:
            dead[k_idx] = True 
            for r in range(x, x + h):
                for c in range(y, y + w):
                    nxt_chase[r][c] = BLANK

    chase = deep_copy(nxt_chase)


# print("*original_chase")
# for row in original_chase:
#     print(*row)
# print()
# for row in chase:
#     print(*row)
# print()
for i, d in cmds:
    i += 2
    move_knights(i, d)
    # print("knights :", knights)
    # print(i-2, "번째 기사 이동 후")
    # print("sum_damage :", sum_damage)
    # print("dead: ", dead)
    # for row in chase:
    #     print(*row)
    # print()
    

answer = 0
for i in range(N+3):
    if not dead[i]:
        answer += sum_damage[i]
print(answer)