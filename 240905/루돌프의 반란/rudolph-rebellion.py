import sys
input = sys.stdin.readline 
from collections import defaultdict

n, m, p, C, D = map(int, input().split())
rudolf = list(map(int, input().split()))
rudolf[0], rudolf[1] = rudolf[0] - 1, rudolf[1] -1
santas = {}
passed = defaultdict(int) # santa_idx : 깨는 시기
dead = [False]*(p+1)
dead[0] = True 
scores = [0]*(1+p)

for _ in range(p):
    pn, sr, sc = map(int, input().split())
    sr, sc = sr - 1, sc - 1
    santas[pn] = [sr, sc]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def santas_move(time):
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0] # 좌하우상 순으로 움직임 
    for i in range(1, p+1):
        # print(time, passed[i])
        if 0 < time < passed[i] or dead[i]:continue 
        min_dir = -1 # 일단 움직이지 않는다 

        sr, sc = santas[i]
        dist = (rudolf[0] - sr)**2 + (rudolf[1] - sc)**2
        min_dist = dist
        for dir in range(4):
            nr, nc = sr + dxs[dir], sc + dys[dir]
            if not in_range(nr, nc) or is_other_santa(nr, nc) != -1:continue 
            tmp_dist = (rudolf[0] - nr)**2 + (rudolf[1] - nc)**2
            if dist > tmp_dist:
                if min_dist >= tmp_dist: 
                    min_dist = tmp_dist
                    min_dir = dir
                    
        if min_dir == -1: continue # 움직이지 않음
        else:
            santas[i] = [sr + dxs[min_dir], sc + dys[min_dir]]
            # 만약 루돌프와 충돌한다면
            # 1. 점수얻기 + 기절 
            # 2. 자신의 반대방향으로 D칸 밀림
            if rudolf == santas[i]:
                scores[i] += D
                passed[i] = time + 2

                now_dir = (min_dir+2)%4
                fr, fc = santas[i][0] + dxs[now_dir]*(D), santas[i][1] + dys[now_dir]*(D) 
                
                # 밀려난 곳이 격자 밖이라면 
                if not in_range(fr, fc): 
                    dead[i] = True 
                # 밀려난 곳에 다른 산타가 있다면 
                else:
                    push_lst = []
                    original_fr, original_fc = fr, fc
                    while is_other_santa(fr, fc) != -1:
                        push_lst.append(is_other_santa(fr, fc))
                        fr += dxs[now_dir]
                        fc += dys[now_dir]

                    santas[i] = [original_fr, original_fc]
                    # 산타 한 칸씩 위치 업데이트 
                    for idx in push_lst:
                        sx, sy = santas[idx]
                        fx, fy = sx + dxs[now_dir], sy + dys[now_dir]
                        if not in_range(fx, fy):
                            dead[idx] = True 
                        else:
                            santas[idx] = [fx, fy]


def get_dist2santas():
    result = [] # (거리, r, c)
    for i in range(1, p+1):
        if not dead[i]:
            r, c = santas[i]
            result.append(((rudolf[0] - r)**2 + (rudolf[1] - c)**2 , r, c))
    return result

def is_other_santa(x, y):
    for k, v in santas.items():
        if dead[k]: continue
        if [x, y] == v:
            return k 
    return -1

def rudolf_move(time):
    global rudolf, santas, dead, passed
    r_dxs, r_dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    # 가장 가까운 산타 찾기
    dist = get_dist2santas()
    dist.sort(key = lambda x:(x[0], -x[1], -x[2]))

    # 해당 산타쪽으로 한 칸 돌진 
    cx, cy = dist[0][1], dist[0][2]
    closest_dir = 0
    min_dist = int(1e9)
    for dir in range(8):
        r_nx, r_ny = rudolf[0] + r_dxs[dir], rudolf[1] + r_dys[dir]
        if not in_range(r_nx, r_ny): continue 

        tmp_dist = (r_nx - cx)**2 + (r_ny - cy)**2
        if min_dist > tmp_dist:
            min_dist = tmp_dist
            closest_dir = dir

    # 루돌프 위치 업데이트
    rudolf = [rudolf[0] + r_dxs[closest_dir], rudolf[1] + r_dys[closest_dir]]

    # 이때 산타 칸으로 간다면 기절 시키고 상호작용 
    # 산타가 기절 
    # 루돌프 -> 산타 : 산타는 C만큼 점수얻고 루돌프 방향으로 C만큼 밀림
    crushed_idx = is_other_santa(rudolf[0], rudolf[1])
    if crushed_idx != -1:
        passed[crushed_idx] = time+2
        scores[crushed_idx] += C 
        # 산타가 C만큼 밀림 
        sx, sy = santas[crushed_idx] 
        fx, fy = sx + r_dxs[closest_dir]*C, sy + r_dys[closest_dir]*C 

        # 밀려난 위치가 격자 밖 : 탈락 
        if not in_range(fx, fy):
            dead[crushed_idx] = True 
        # 밀려난 위치에 다른 산타 : 상호작용 
        else:
            push_lst = []
            original_fx, original_fy = fx, fy
            while is_other_santa(fx, fy) != -1:
                push_lst.append(is_other_santa(fx, fy))
                fx += r_dxs[closest_dir]
                fy += r_dys[closest_dir]
            
            santas[crushed_idx] = [original_fx, original_fy]
            # 산타 한 칸씩 위치 업데이트 
            for idx in push_lst:
                sx, sy = santas[idx]
                fx, fy = sx + r_dxs[closest_dir], sy + r_dys[closest_dir]
                if not in_range(fx, fy):
                    dead[idx] = True 
                else:
                    santas[idx] = [fx, fy]



def game_over():
    for i in range(p+1):
        if dead[i] == False:
            return False
    return True 

def give_score():
    for i in range(1, p+1):
        if not dead[i]: scores[i] += 1


for time in range(1, m+1):
    if game_over(): break 
    rudolf_move(time)
    # print(rudolf)
    santas_move(time)
    # print(santas)
    # print(passed)
    # print("dead = ", dead, "// passed = ", passed)
    give_score()
    # print()

print(*scores[1:])