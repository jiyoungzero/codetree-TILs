import sys
input = sys.stdin.readline 
from collections import defaultdict

Q = int(input())
cmds = []
for _ in range(Q):
    cmds.append(list(map(int, input().split())))
N, M, P, K, S, L = 0,0,0,0,0,0
rabbits = [] # 고유번호, 이동거리
counts = {}
scores = {}
pos = {}

N, M, P = cmds[0][1], cmds[0][2], cmds[0][3]
lst = cmds[0][4:]
for i in range(len(lst)//2):
    a, b = lst.pop(), lst.pop()
    rabbits.append((b, a))
for rabbit in rabbits:
    pos[rabbit[0]] = (0,0)
    counts[rabbit[0]] = 0
    scores[rabbit[0]] = 0


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M 

def match_pid_dist(pid):
    for rabbit in rabbits:
        if rabbit[0] == pid:
            return rabbit[1]
    return False

def pick_move_rabbit():
    global counts
    lst = []
    for k, v in counts.items():
        lst.append((v, pos[k][0]+pos[k][1], pos[k][0], pos[k][1], k))
    lst.sort(key = lambda x:(x[0], x[1], x[2], x[3], x[4]))
    target_pid = lst[0][-1]
    counts[target_pid] += 1

    return target_pid

def move(rabbit_pid):
    global pos, scores, rabbits, counts
    
    dxs, dys = [-1, 0, 1, 0],[0, 1, 0, -1] # 상 우 하 좌
    d_lst = []
    
    for dir in range(4):
        x, y = pos[rabbit_pid]
        dx, dy = dxs[dir], dys[dir]
        for dist in range(match_pid_dist(rabbit_pid)):
            if not in_range(x + dx, y + dy):
                dx = -dx
                dy = -dy
            nx, ny = x + dx, y + dy
            x, y = nx, ny
        d_lst.append((x+y, x, y))
    d_lst.sort(key = lambda x :(-x[0], -x[1], -x[2]))
    final_x, final_y = d_lst[0][1], d_lst[0][2]
    pos[rabbit_pid] = (final_x, final_y)
    
    # pid를 제외한 토끼의 점수 얻기
    for k in scores.keys():
        if k == rabbit_pid:continue
        else:
            scores[k] += (final_x+final_y+2)
    return 
            
def get_S_score():
    lst = []
    for k, v in pos.items():
        lst.append((v[0]+v[1], v[0], v[1], k, counts[k]))
    lst.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    cur = 0
    flag = False
    while lst[cur][-1] == 0:
        cur += 1
        flag = True
    if flag: cur -= 1 

    target_pid = lst[cur][3]
    scores[target_pid] += S 
    return 
       

def simulate():
    global K
    for time in range(K):
        rabbit_pid = pick_move_rabbit()
        # print(time, "번째 선택 =", rabbit_pid)
        move(rabbit_pid)
        # print("이동 후 = ", pos, " 점수 =", scores)
    get_S_score()
    # print("scores : ", scores)
    # print("counts :", counts)
    # print("pos :", pos)


for c in range(Q):
    if cmds[c][0] == 100:
        continue
    elif cmds[c][0] == 200:
        K, S = cmds[c][1], cmds[c][2]
        simulate()
    elif cmds[c][0] == 300:
        pid_target, L = cmds[2][1], cmds[2][2]
        for i, rabbit in enumerate(rabbits):
            if rabbit[0] == pid_target:
                rabbits[i] = (pid_target, L*rabbit[1])
    else:
        max_score = 0
        for tmp in scores.values():
            if tmp > max_score:
                max_score = tmp
        print(max_score)