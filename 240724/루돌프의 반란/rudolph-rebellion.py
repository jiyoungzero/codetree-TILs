import sys
input = sys.stdin.readline 
from collections import deque
 
r_dxs, r_dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌

n, m, p, C, D = map(int, input().split())
rudolf = list(map(int, input().split()))
rudolf[0] -= 1
rudolf[1] -= 1
santas = {}
now_k = 0
is_passed_out = [0]*(1+p)
is_dead = [False]*(1+p)

ini_santas = []
for _ in range(p):
    pn, sr, sc = map(int, input().split())
    ini_santas.append([pn, sr-1, sc-1])
ini_santas.sort()
for pn, sr, sc in ini_santas:
    santas[pn] = [sr, sc]
answer = [0]*(p+1)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_dist(r1, c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2


def push_santa(idx, dir):
    global santas, is_dead, is_passed_out
    sr, sc = santas[idx]
    # 밀림 + 점수 주기
    n_sr, n_sc = sr + r_dxs[dir]*C, sc + r_dys[dir]*C
    answer[idx] += C
    # print(idx, "번째 산타 밀림 ->", (n_sr, n_sc), answer[idx])

    # 격자 밖이라면 탈락 
    if not in_range(n_sc, n_sr):
        is_dead[idx] = True
        return 

    # 기절시키기
    is_passed_out[idx] = now_k + 2

    # 밀린 산타 위치 업데이트
    sr, sc = n_sr, n_sc
    santas[idx] = [sr,sc]

    # 상호작용하는지 보기
    chains = []
    que = deque()
    que.append(idx)
    while que:
        cur_idx = que.popleft()
        cur_sr, cur_sc = santas[cur_idx][0], santas[cur_idx][1]
        for k, santa in santas.items():
            if is_dead[k]: continue
            if k in chains: continue
            if k != idx and cur_sr == santa[0] and cur_sc == santa[1]:
                que.append(k)
                chains.append(k)
    # 상호작용 했다면 같이 밀린 산타 위치 업데이트
    if chains:
        move = 1
        for i in chains:
            x, y = santas[i]
            nx, ny = sr + r_dxs[dir]*move, sc + r_dys[dir]*move
            if not in_range(nx, ny): is_dead[i] = True # 격자 밖으로 밀려나면
            else:
                santas[i] = [nx, ny]
                move += 1
    
def rudolf_move():
    global rudolf
    lst = []
    close_santas = []
    
    for k, santa in santas.items():
        if is_dead[k]:continue            
        dist = get_dist(rudolf[0], rudolf[1], santa[0], santa[1])
        close_santas.append((dist, santa[0], santa[1], k))
    close_santas.sort(key = lambda x:(x[0], -x[1], -x[2]))
    closest_santa_idx = close_santas[0][3]
 
    # 제일 가까운 이동 방향 찾기 
    close_dir = 0
    dist = int(1e9)
    for dir in range(8):
        nx, ny = rudolf[0]+r_dxs[dir], rudolf[1] + r_dys[dir]
        if not in_range(nx, ny):continue
        tmp = get_dist(nx, ny, santas[closest_santa_idx][0], santas[closest_santa_idx][1])
        if tmp < dist:
            dist = tmp
            close_dir = dir
        
    # 루돌프 위치 업데이트 
    rudolf[0] += r_dxs[close_dir]
    rudolf[1] += r_dys[close_dir]

    # 산타와의 충돌 검사
    if dist == 0: # 충돌햇다면
        push_santa(closest_santa_idx, close_dir) # idx번째 산타를 dir방향으로 C칸 밀기
    return 

def meet(x, y, idx):
    for k, santa in santas.items():
        if is_dead[k]:continue
        if k != idx and [x, y] == santa:return True
    return False

def crush2rudolf(idx, dir):
    global santas, is_dead, is_passed_out
    sr, sc = santas[idx]
    # 밀림 + 점수 주기
    n_sr, n_sc = sr + dxs[dir]*(max(0, D-1)), sc + dys[dir]*(max(0, D-1))
    answer[idx] += D

    # 격자 밖이라면 탈락 
    if not in_range(n_sc, n_sr):
        is_dead[idx] = True
        return 

    # 기절시키기 
    is_passed_out[idx] = now_k + 2
    
    # 밀린 산타 위치 업데이트
    sr, sc = n_sr, n_sc
    santas[idx] = [sr,sc]   

    # 상호작용하는지 보기
    chains = []
    que = deque()
    que.append(idx)
    while que:
        cur_idx = que.popleft()
        cur_sr, cur_sc = santas[cur_idx][0], santas[cur_idx][1]
        for k, santa in santas.items():
            if is_dead[k]: continue
            if k in chains: continue
            if k != idx and cur_sr == santa[0] and cur_sc == santa[1]:
                que.append(k)
                chains.append(k)

    # 상호작용 했다면 같이 밀린 산타 위치 업데이트
    if chains:
        move = 1
        for i in chains:
            x, y = santas[i]
            nx, ny = sr + dxs[dir]*move, sc + dys[dir]*move
            if not in_range(nx, ny): is_dead[i] = True # 격자 밖으로 밀려나면
            else:
                santas[i] = [nx, ny]
                move += 1
    return 


def santas_move():
    global santas, is_dead, is_passed_out

    for k, santa in santas.items():
        if is_dead[k]:continue 
        if is_passed_out[k]: continue
        x, y = santa
        
        now_d = get_dist(x, y, rudolf[0], rudolf[1])
        lst = []
        crushed = False
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue
            if meet(nx, ny, k): continue
            d = get_dist(nx, ny, rudolf[0], rudolf[1])
            if now_d > d:
                # print(k, "루돌프와 충돌 ", rudolf, nx, ny)
                if d == 0: # 루돌프와 충돌하는 경우
                    # print(k, "루돌프와 충돌 ", rudolf, nx, ny)
                    crush2rudolf(k, (dir+2)%4) 
                    crushed = True
                else: # 충돌안하는 경우 위치 업데이트
                    santas[k] = [nx, ny]
                    lst.append((d, dir, nx, ny))
        if not crushed and lst:
            lst.sort(key = lambda x :(x[0], x[1]))
            santas[k] = [lst[0][2], lst[0][3]]

for k in range(1, m+1):
    now_k = k
    # passed_out 관리
    for i in range(1, 1+p):
        if is_passed_out[i] == k:
            is_passed_out[i] = 0
    if all(is_dead[1:]):break

    rudolf_move()
    # print(k, "턴")
    # print("rudolf 이동 후 = ", rudolf )
    santas_move()  
    # print("santas 이동 후 = ", santas)
    # print("탈락 했는지 =", is_dead)

    # 탈락하지 않은 산타 1점씩 추가 부여
    for k in santas.keys():
        if not is_dead[k]:
            answer[k] += 1
    # print("scores = ", *answer[1:])
    # print()
        

print(*answer[1:])