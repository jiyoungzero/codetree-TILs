import sys
input = sys.stdin.readline 
from collections import deque, defaultdict

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# meeting = [[0]*10 for _ in range(10)] # arr[i][j] : i와 맞닿은 j의 변의 개수
dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = [[False]*n for _ in range(n)] 
group_num = [[0]*n for _ in range(n)]
group_cnt = [[0]*n for _ in range(n)]

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def ele_rotate(size, sx, sy, i, j):
    oi, oj = i-sx, j-sy
    ri, rj = oj, size - oi - 1
    fi, fj = ri + sx, rj + sy 
    return (fi, fj)

def all_rotate(): # 십자 모양 반시계 방향 회전 + 4개 정사각형 시계방향 회전 
    global arr
    nxt_arr = deep_copy(arr)
    # print("회전 전")
    # for row in arr:
    #     print(*row)
    
    prev_arr = deep_copy(arr)
    # 십자가 모양 반시계 
    for _ in range(3):
        for i in range(n):
            si, sj = i, n//2
            fi, fj = ele_rotate(n, 0, 0, si, sj)
            nxt_arr[fi][fj] = prev_arr[si][sj]
        for j in range(n):
            si, sj = n//2, j 
            fi, fj = ele_rotate(n, 0, 0, si, sj)
            nxt_arr[fi][fj] = prev_arr[si][sj] 
        prev_arr = deep_copy(nxt_arr)
    # print("십자가 회전 후")
    # for row in nxt_arr:
    #     print(*row)
    # print()
    # 4개 정사각형 시계방향 회전 
    # 1. 좌상 
    for i in range(n//2):
        for j in range(n//2):
            fi, fj = ele_rotate(n//2, 0, 0, i, j)
            nxt_arr[fi][fj] = arr[i][j]
    # print("좌상")
    # for row in nxt_arr:
    #     print(*row)
    # print()
    # 2. 우사
    for i in range(n//2):
        for j in range(n//2+1, n):
            fi, fj = ele_rotate(n//2, 0, n//2+1, i, j)
            nxt_arr[fi][fj] = arr[i][j]
    
    # 3. 좌하
    for i in range(n//2+1, n):
        for j in range(n//2):
            fi, fj = ele_rotate(n//2, n//2+1, 0 , i, j)
            nxt_arr[fi][fj] = arr[i][j]

    # 4. 우하
    for i in range(n//2+1, n):
        for j in range(n//2+1, n):
            fi, fj = ele_rotate(n//2, n//2+1, n//2+1, i, j)
            nxt_arr[fi][fj] = arr[i][j]

    arr = deep_copy(nxt_arr)



def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def bfs(x, y):
    global visited
    pos = [(x, y)]
    que = deque()
    que.append((x, y))
    visited[x][y] = True 

    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                pos.append((nx, ny))
                visited[nx][ny] = True 
                que.append((nx, ny))
    return pos 

def get_groups():
    global answer, visited
    groups = []
    # (숫자 : 칸 수)
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                pos = bfs(i, j)
                a_num = arr[i][j]
                groups.append((a_num, pos))
    return groups

def grading(groups): # 맞닿은 부분 계산해서 예술성 더하기 
    global group_num, group_cnt, answer
    for group in groups:
        cnt = len(group[1])
        for x, y in group[1]:
            group_num[x][y] = group[0]
            group_cnt[x][y] = cnt 
    # print("group_num")
    # for row in group_num:
    #     print(*row)
    # print("group_cnt")
    # for row in group_cnt:
    #     print(*row)
    tmp = 0
    for i in range(n):
        for j in range(n):
            a_num = arr[i][j]
            a_cnt = group_cnt[i][j]
            for dir in range(4):
                ni, nj = i + dxs[dir], j + dys[dir]
                if not in_range(ni, nj):
                    continue 
                if arr[i][j] != arr[ni][nj]:
                    b_num, b_cnt = arr[ni][nj], group_cnt[ni][nj]
                    tmp += (a_cnt + b_cnt)*a_num*b_num 
    tmp //= 2
    # print(tmp)
    answer += tmp
                
                

grading(get_groups())
for _ in range(3):
    # print("--회전 전--")
    # for row in arr:
    #     print(*row)
    # print()
    all_rotate()
    # print("--회전 후--")
    # for row in arr:
    #     print(*row)
    # print()
    visited = [[False]*n for _ in range(n)] 
    group_num = [[0]*n for _ in range(n)]
    group_cnt = [[0]*n for _ in range(n)]
    grading(get_groups())


print(answer)