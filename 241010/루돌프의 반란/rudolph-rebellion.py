import sys
input = sys.stdin.readline 
from collections import deque

n, m, p, c, d = map(int, input().split())
rudolf = list(map(int, input().split()))
rudolf[0] -= 1
rudolf[1] -= 1
arr = [[0]*n for _ in range(n)]
arr[rudolf[0]][rudolf[1]] = -2 # 루돌프의 위치는 -2
is_passedout = [0]*(p+1) # 양수면 기절함 (양수의 파라미터가 깨어나는 시간) 
is_dead = [False]*(p+1) # 게임판 밖으로 밀려남 

santas = {}
for _ in  range(1, p+1):
    idx, sr, sc = map(int, input().split())
    santas[idx] = [sr-1, sc-1]
    arr[sr-1][sc-1] = idx # 산타의 idx로 위치 
scores = [0]*(1+p)

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def get_dist(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def rudolf_move(round_idx):
    global rudolf, arr
    # 가장 가까운 산타 찾기 
    candidates = [] # (거리, r, c)
    for s_idx in range(1, p+1):
        if is_dead[s_idx]:continue
        sr, sc = santas[s_idx]
        candidates.append((get_dist(rudolf[0], rudolf[1], sr, sc), sr, sc, s_idx))
    candidates.sort(key = lambda x:(x[0], -x[1], -x[2]))
    # 움직일 방향
    _, sr, sc, s_idx = candidates[0]
    rr, rc = rudolf[0], rudolf[1]
    dxs, dys = 0, 0

    if sr < rr:
        dxs = -1
    if sr > rr :
        dxs = 1
    
    if sc < rc:
        dys = -1
    if sc > rc:
        dys = 1
    
    # 루돌프 움직임
    arr[rudolf[0]][rudolf[1]] = 0
    rudolf = [rudolf[0] + dxs, rudolf[1] + dys]
    # arr[rudolf[0]][rudolf[1]] = -2

    # 충돌하는 경우
    if get_dist(rudolf[0], rudolf[1], sr, sc) == 0:
        # 해당 산타 점수 얻기 + 기절 
        # print(s_idx, "충돌")
        scores[s_idx] += c 
        is_passedout[s_idx] = round_idx + 2
        # 해당 산타의 c만큼 dxs, dys방향으로 이동
        n_sr, n_sc = sr + dxs*c, sc + dys*c 
        if not in_range(n_sr, n_sc): 
            arr[sr][sc] = 0
            is_dead[s_idx] = True 
        else:
            # 다른 산타와 상호작용할 때
            if arr[n_sr][n_sc] > 0:
                pushing_list = [arr[n_sr][n_sc]]
                que = deque()
                que.append((n_sr, n_sc))
                while que:
                    x, y = que.popleft()
                    nx, ny = x + dxs, y + dys
                    if not in_range(nx, ny):
                        idx = arr[x][y]
                        pushing_list.pop() # 어차피 밖으로 밀려나므로
                        is_dead[idx] = True
                        continue 
                    if arr[nx][ny] > 0:
                        pushing_list.append(arr[nx][ny])
                        que.append((nx, ny))
                # pushing_lst에 있는 산타 pop해서 한 칸씩 옮기기
                while pushing_list:
                    i = pushing_list.pop()
                    # print(s_idx, santas, pushing_list)
                    x, y = santas[i]
                    nx, ny = x+ dxs, y + dys

                    arr[x][y] = 0
                    arr[nx][ny] = i 
                    santas[i] = [nx, ny]  
            # else: # 그냥 밀쳐지기만 할 때 
            arr[sr][sc] = 0
            santas[s_idx] = [n_sr, n_sc]
            arr[n_sr][n_sc] = s_idx
    arr[rudolf[0]][rudolf[1]] = -2

     
def santas_move(round_idx):
    global arr, santas, is_passedout

    for s_idx in range(1, p+1):
        if is_passedout[s_idx] > 0 or is_dead[s_idx]: continue 
        sr, sc = santas[s_idx]
        original_sr, original_sc = sr, sc
        original_dist = get_dist(rudolf[0], rudolf[1], sr, sc)
        dxs, dys = 0, 0
        sdxs, sdys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
        candidates = []
        # print(p+1, s_idx, is_dead, is_passedout)
        for dir in range(4):
            n_sr, n_sc = sr + sdxs[dir], sc + sdys[dir]
            if not in_range(n_sr, n_sc) or arr[n_sr][n_sc] > 0:continue 
            tmp_dist = get_dist(rudolf[0], rudolf[1], n_sr, n_sc)
            if original_dist > tmp_dist:
                candidates.append((tmp_dist, dir))
        # 움직일 수 있는 칸이 없다면 그냥 통과 
        if len(candidates) == 0: continue 

        candidates.sort(key = lambda x:(x[0], x[1]))
        dxs, dys = -sdxs[candidates[0][1]], -sdys[candidates[0][1]]
        sdxs, sdys = -dxs, -dys
        # print(s_idx, (original_sr, original_sc), (sr+sdxs, sc+sdys))

        # 만약 루돌프와 충돌한다면 
        if get_dist(rudolf[0], rudolf[1], sr + sdxs, sc + sdys) == 0:
            # d만큼 점수 얻고, 기절
            scores[s_idx] += d 
            is_passedout[s_idx] = round_idx + 2
            # d만큼 이동 
            final_sr, final_sc = sr + dxs*(d-1), sc + dys*(d-1)
            # 게임 밖일 때
            if not in_range(final_sr, final_sc):
                is_dead[s_idx] = True 
                arr[original_sr][original_sc] = 0 
                continue
            
            # 상호작용하는지
            if arr[final_sr][final_sc] > 0 and s_idx != arr[final_sr][final_sc]:
                pushing_list = [arr[final_sr][final_sc]]
                que = deque()
                que.append((final_sr, final_sc))
                # print(santas, pushing_list)
                while que:
                    x, y = que.popleft()
                    nx, ny = x + dxs, y + dys
                    if not in_range(nx, ny):
                        is_dead[arr[x][y]] = True 
                        pushing_list.pop()
                        continue 
                    if arr[nx][ny] > 0:
                        pushing_list.append(arr[nx][ny])
                        que.append((nx, ny))
                # print(pushing_list, final_sr, final_sc, (dxs, dys))
                while pushing_list:
                    i = pushing_list.pop()
                    x, y = santas[i]
                    nx, ny = x + dxs, y + dys
                    # print((x, y), "->", (nx, ny))
                    arr[nx][ny] = arr[x][y]
                    santas[arr[x][y]] = [nx, ny]
                    arr[x][y] = 0

            # 밀쳐진 산타 위치 업데이트 
            arr[original_sr][original_sc] = 0
            arr[final_sr][final_sc] = s_idx 
            santas[s_idx] = [final_sr, final_sc]

        # 충돌하지 않는다면 
        else:
            final_sr, final_sc = sr + sdxs, sc + sdys
            arr[original_sr][original_sc] = 0
            arr[final_sr][final_sc] = s_idx 
            santas[s_idx] = [final_sr, final_sc]


def wakeup_santas(round_idx):
    for s_idx in range(1, p+1):
        if is_passedout[s_idx] == round_idx:
            is_passedout[s_idx] = 0

for round_idx in range(1, m+1):
    wakeup_santas(round_idx)
    # print(round_idx,"=====")
    # for row in arr:
    #     print(*row)
    if all(is_dead[1:]):break
    rudolf_move(round_idx)
    # print("rudolf 움직인 후")
    # for row in arr:
    #     print(*row)
    if all(is_dead[1:]):break
    santas_move(round_idx)
    # print("산타 움직임 후")
    # for row in arr:
    #     print(*row)
    # print()
    for i in range(1, p+1):
        if not is_dead[i]:
            scores[i] += 1

print(*scores[1:])