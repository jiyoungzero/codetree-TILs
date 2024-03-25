import sys
input = sys.stdin.readline
from collections import deque
import copy 
BLANK = 0
WALL = 2
TRICK = 1
dxs, dys = [-1,0,1,0], [0,1,0,-1] # 위쪽, 오른쪽, 아래쪽, 왼쪽

L, N, Q = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(L)]
w_board = [[0]*L for _ in range(L)]
warriers = [0]
original_warriers_k = [0]
for idx in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    warriers.append((idx, r, c, h, w, k, True))
    original_warriers_k.append(k)
    for row in range(r, r+h):
        for col in range(c, c+w):
            w_board[row][col] = idx 
cmds = []
for _ in range(Q):
    i, d = map(int, input().split())
    cmds.append((i, d))

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L

def get_move_pos(warrier, d):
    result = []
    idx, r, c, h, w, k, _ = warrier
    visited = [[False]*L for _ in range(L)]
    que = deque()
    for row in range(r, r+h):
        for col in range(c, c+w):
            que.append((row, col))
            visited[row][col] = True
            result.append((row, col, idx))
    
    while que:
        x, y = que.popleft()
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and board[nx][ny] == WALL: continue
        if in_range(nx, ny) and not visited[nx][ny] and w_board[nx][ny] != idx and w_board[nx][ny] > 0:
            other_warrier_idx = w_board[nx][ny]
            idx, r, c, h, w, k, survive = warriers[other_warrier_idx]
            if survive: # 살아있는 기사만 이동 가능하므로
                for row in range(r, r+h):
                    for col in range(c, c+w):           
                        que.append((row, col))
                        visited[row][col] = True 
                        result.append((row, col, idx))
    return result

def possible_move(move_pos, d):
    for x, y, _ in move_pos:
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny) or board[nx][ny] == WALL:
            return False
    return True

def warrier_move(warrier, d):
    global w_board
    idx, r, c, h, w, k, _ = warrier
    cmd_w_idx = idx
    nxt_w_board = [[0]*L for _ in range(L)]

    # 해당 기사가 이동하는 방향으로 마주치는 warrier의 pos
    move_pos = get_move_pos(warrier, d)
    if possible_move(move_pos, d):
        for x, y, w_idx in move_pos:
            nx, ny = x + dxs[d], y + dys[d]
            nxt_w_board[nx][ny] = w_idx

        # 안 움직이는 애들도 nxt_w_board에 표시
        # warriers 배열 내에서의 업데이트
        move_idx = set([pos[2] for pos in move_pos])
        for update_idx in move_idx:
            update_idx, update_r, update_c, update_h, update_w, update_k, _ = warriers[update_idx]
            warriers[update_idx] = (update_idx, update_r+dxs[d], update_c+dys[d], update_h, update_w, update_k, True)
        for warrier in warriers[1:]:
            if warrier[-1] and warrier[0] not in move_idx:
                not_move_idx, not_move_r, not_move_c, not_move_h, not_move_w, not_move_k, _ = warrier
                for row in range(not_move_r, not_move_r+not_move_h):
                    for col in range(not_move_c, not_move_c + not_move_w):
                        nxt_w_board[row][col] = not_move_idx

        w_board = copy.deepcopy(nxt_w_board)
    
        trick_warrier(move_idx,cmd_w_idx) # 이동한 위치 내에서의 트릭 수만큼 체력 소모 
    return

def trick_warrier(move_idx, cmd_w_idx):
    for i in move_idx:
        if i == cmd_w_idx:
            continue
        idx, r, c, h, w, k, survive = warriers[i]
        trick_cnt = 0

        for row in range(r, r+h):
            for col in range(c, c+w):
                if board[row][col] == TRICK:
                    trick_cnt += 1
        if k - trick_cnt <= 0:
            warriers[i] = (i, r, c, h, w, k-trick_cnt, False)
        else:
            warriers[i] = (i, r, c, h, w, k-trick_cnt, True)

for cmd in cmds:
    i, d = cmd
    if warriers[i][-1]: # 생존한 기사만 이동
        warrier_move(warriers[i], d)
    
    # for row in w_board:
    #     print(*row)
    # print()
    # for warrier in warriers[1:]:
    #     print(warrier[-2], end=", ")
    # print()
    # print()


answer = 0
for i in range(1, N+1):
    if warriers[i][-1]:
        answer += (original_warriers_k[i]-warriers[i][-2])
print(answer)