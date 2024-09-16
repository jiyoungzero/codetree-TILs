import sys
input = sys.stdin.readline 

Q = int(input())
rabbits = {}
pos = {}
N, M, P, K, S = 0, 0, 0, 0, 0
pid_t, L = 0, 0
jump_cnt = {}
scores = {}

for _ in range(Q):
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 100:
        N, M, P = cmd[1], cmd[2], cmd[3]
        for i in range(4, len(cmd), 2):
            pid, p_d = cmd[i], cmd[i+1]
            rabbits[pid] = p_d
            pos[pid] = [0, 0]
            jump_cnt[pid] = 0
            scores[pid] = 0
    elif cmd[0] == 200:
        K, S = cmd[1], cmd[2]
    elif cmd[0] == 300:
        pid_t, L = cmd[1], cmd[2]

arr = [[0]*M for _ in range(N)]

def get_primary_rabbit():
    lst = []
    for (k1, v1), (k2, v2) in zip(jump_cnt.items(), pos.items()):
        lst.append((v1, v2[0] + v2[1] + 2, v2[0]+1, v2[1]+1, k2))
    lst.sort()
    return lst[0][-1]
 

# for _ in range(K):
#     get_primary_rabbit()    
print(get_primary_rabbit())