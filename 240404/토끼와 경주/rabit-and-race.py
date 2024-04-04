from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline 

Q = int(input())
N, M, P = 0, 0, 0
heap = []
dist = defaultdict()
score = defaultdict()
minus_score = 0
dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]

def init(cmd):
    global N, M, P
    N = cmd[0]
    M = cmd[1]
    P = cmd[2]
    for i in range(3, len(cmd)):
        if i%2 == 1:
            heapq.heappush(heap, [0,0,0,0,cmd[i]])
            dist[cmd[i]] = cmd[i+1]
            score[cmd[i]] = 0
    return 

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M 

def out_of_range(nx, ny):
    nx %= 2*(N-1)
    ny %= 2*(M-1)
    return min(nx, 2*(N-1)-nx), min(ny, 2*(M-1)-ny)

def most_row_col_pos(positions):
    result = []
    positions.sort(key = lambda x : -(x[0]+x[1]))
    max_value = positions[0][0] + positions[0][1]
    for position in positions:
        if position[0]+position[1] == max_value:
            result.append(position)
        else:break
    return result

def most_row(positions):
    result = []
    positions.sort(key = lambda x : -x[0])
    max_value = positions[0][0]
    for position in positions:
        if position[0] == max_value:
            result.append(position)
        else:break
    return result 

def most_col(positions):
    positions.sort(key = lambda x : -x[1])
    return positions[0]

def select_position(positions):
    positions = most_row_col_pos(positions)
    if len(positions) == 1:
        return positions[0]
    
    positions = most_row(positions)
    if len(positions) == 1:
        return positions[0]
    
    positions = most_col(positions)
    return positions
    
def addScores(nx, ny, id):
    global minus_score
    minus_score += (-nx-ny-2)
    score[id] += (-nx-ny-2)

def simulate(cmd):
    K, S = cmd[0], cmd[1]

    select_rabbit = []
    for _ in range(K):
        jump, s, x, y, pid = heapq.heappop(heap)
        jump += 1
        
        positions = []
        for i in range(4):
            nx, ny = x + dxs[i]*dist[pid], y+dys[i]*dist[pid]
            if not in_range(nx, ny):
                nx, ny = out_of_range(nx, ny)
            positions.append((nx, ny))
        nx, ny = select_position(positions)
        addScores(nx, ny, pid)
        heapq.heappush(select_rabbit, [-(nx+ny), -nx, -ny, -pid])
        heapq.heappush(heap, [jump, nx+ny, nx, ny, pid])
    _,_,_, pid = heapq.heappop(select_rabbit)

    score[-pid] += S 
    return 

def changeDist(cmd):
    pid, L = cmd[0], cmd[1]
    dist[pid] *= L 
    return 

def get_max_score():
    result = -1
    for s in score.values():
        if s > result:
            result = s 
    return result - minus_score

for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 100:
        init(cmd[1:])
    elif cmd[0] == 200:
        simulate(cmd[1:])
    elif cmd[0] == 300:
        changeDist(cmd[1:])
    else:
        print(get_max_score())