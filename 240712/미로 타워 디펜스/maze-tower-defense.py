import sys
input = sys.stdin.readline 
import copy
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
attacks = [tuple(map(int, input().split())) for _ in range(m)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def attack_monster(d, p):
    global answer
    x, y = n//2, n//2
    for _ in range(p):
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):break
        answer += arr[nx][ny]
        # print("초반 공격 점수 = ", arr[nx][ny])
        arr[nx][ny] = 0
        x, y = nx, ny


def in_pop_lst(idx, pop_lst):
    for start, end in pop_lst:
        if start <= idx < end:
            return True
    return False

def arr2line():
    m_dxs, m_dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    sx, sy = n//2, n//2
    lst = []
    
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    while True:
        if (sx, sy) == (0,0):break
        for dir in range(4):
            if dir == 0 or dir == 2:
                cnt += 1
            for _ in range(cnt):
                nx, ny = sx + m_dxs[dir], sy + m_dys[dir]
                if not in_range(nx, ny):break
                if visited[nx][ny]:break
                visited[nx][ny] = True
                if arr[nx][ny] > 0:
                    lst.append(arr[nx][ny])
                sx, sy = nx, ny
            if (sx, sy) == (0, 0):break
    return lst

def popping(lst):
    global arr, answer
    n_arr = [[0]*n for _ in range(n)]

    pop_lst = []
    pop_flag = False
    prefix = lst[0]
    dup = 1
    for i, ele in enumerate(lst[1:]):
        if ele == prefix:
            dup += 1
        else:
            if dup >= 4:
                pop_flag = True
                pop_lst.append((i-dup+1, min(len(lst), i+1)))
                answer += (prefix*dup)
                # print("중복 폭탄 점수 = ", prefix*dup)
            dup = 1
        prefix = ele

    final_lst = []
    for i, ele in enumerate(lst):
        if in_pop_lst(i, pop_lst):continue
        final_lst.append(ele)

    return (final_lst, pop_flag)
    

def line2arr(final_lst): 
    global arr
    n_arr = [[0]*n for _ in range(n)]
    sx, sy = n//2, n//2
    que = deque(final_lst)

    m_dxs, m_dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    cnt = 0
    while True:
        if (sx, sy) == (0, -1):break
        if not que:break
        
        for dir in range(4):
            if not que: break
            if dir == 0 or dir == 2:
                cnt += 1

            for _ in range(cnt):
                if not que: break
                ele = que.popleft()
                nx, ny = sx + m_dxs[dir], sy + m_dys[dir]
                if not in_range(nx, ny):break

                n_arr[nx][ny] = ele
                sx, sy = nx, ny

    # arr 업데이트
    arr = copy.deepcopy(n_arr)


def get_input_arr(lst):
    nxt_lst = []
    lst.append(0)

    cnt = 1
    prefix = lst[0]
    for i, ele in enumerate(lst[1:]):
        if ele == prefix:
            cnt += 1
        else:
            nxt_lst += [cnt, prefix]
            cnt = 1
        prefix = ele 
    return nxt_lst


for time in range(m):
    d, p = attacks[time]
    attack_monster(d, p)
    lst = arr2line()

    while True:
        nxt_lst, flag = popping(lst)
        if not flag:
            break
        lst = nxt_lst
    
    # print("--",get_input_arr(lst))
    line2arr(get_input_arr(lst))
    # for row in arr:
    #     print(*row)
    # print()



print(answer)
# for row in arr:
#     print(*row)
# print()
# attack_monster(attacks[0][0], attacks[0][1]+4)

# for row in arr:
#     print(*row)