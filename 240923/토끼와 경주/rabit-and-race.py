import sys
input = sys.stdin.readline 
import heapq


n = int(input())
cmds = [list(map(int, input().split())) for _ in range(n)]
rabbits = {}
N, M, P = 0, 0, 0
K, S = 0, 0
jump_cnts = {}
scores = {}

def pick_rabbit():
    lst = []
    for ids, cnts in jump_cnts.items():
        lst.append((cnts, ids))
    for i, (cnts, ids) in enumerate(lst):
        values = rabbits[ids]
        lst[i] = ((cnts, values[1]+values[2], values[1], values[2], ids))
    heap = []
    for ele in lst:
        heapq.heappush(heap, ele)
    result = heapq.heappop(heap)

    return result[-1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def out_of_range(nx, ny):
    nx %= 2*(N-1)
    ny %= 2*(M-1)
    return min(nx, 2*(N-1)-nx), min(ny, 2*(M-1)-ny)

def simulate():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    i = pick_rabbit()

    move_cnt, x, y = rabbits[i]
    jump_cnts[i] += 1

    nxt_pos = []
    for dir in range(4):
        nx, ny = x + dxs[dir]*move_cnt, y + dys[dir]*move_cnt
        if not in_range(nx, ny):
            nx, ny = out_of_range(nx, ny)
        nxt_pos.append((nx + ny, nx, ny))
    nxt_pos.sort(key = lambda x:(-x[0], -x[1], -x[2]))

    # 최종 위치로 이동
    final_pos = (nxt_pos[0][1], nxt_pos[0][2])
    rabbits[i][1], rabbits[i][2] = final_pos 

    # p-1마리 점수 획득 
    plus = final_pos[0] + final_pos[1] + 2
    for k in scores.keys():
        if k == i:continue 
        scores[k] += plus
    

def plus_S():
    heap = []
    for k, v in rabbits.items():
        heapq.heappush(heap, (-v[1]-v[2], -v[1], -v[2], -k))
    
    while heap:
        cur = heapq.heappop(heap)
        idx = -cur[-1]
    
        if jump_cnts[idx] != 0:
            scores[idx] += S 
            break


for cmd in cmds:
    if cmd[0] == 100:
        N, M, P = cmd[1], cmd[2], cmd[3]
        for i in range(4, len(cmd)-1, 2):
            rabbits[cmd[i]] = [cmd[i+1], 0, 0]
            jump_cnts[cmd[i]] = 0
            scores[cmd[i]] = 0

    elif cmd[0] == 200:
        K, S = cmd[1], cmd[2]
        for _ in range(K):
            simulate()
        plus_S()

    elif cmd[0] == 300:
        origin = rabbits[cmd[1]][0]
        rabbits[cmd[1]][0] = origin*cmd[2]

answer = 0
for v in scores.values():
    answer = max(answer, v)
print(answer)