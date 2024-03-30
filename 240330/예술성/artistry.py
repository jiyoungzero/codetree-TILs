import sys, copy
input = sys.stdin.readline 
from itertools import combinations 
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# a, b 그룹의 조화로움 계산
# (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수

# 초기 예술 점수 
# 시계방향 회전 
# 기준 : x, y (0,2) -> (2, 4) n = 5
# 회전 후 : x, y = y, n - x - 1
answer = 0
dxs, dys = [0,0,1,-1], [1,-1,0,0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy, target_num):
    global visited
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = True 
    
    pos = [(sx, sy)]
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):
                continue 
            if not visited[nx][ny] and target_num == arr[nx][ny]:
                pos.append((nx, ny))
                visited[nx][ny] = True
                que.append((nx, ny))
    return pos    

def find_group_pos():
    global groups, visited
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(bfs(i,j, arr[i][j]))

def get_art_grade(A, B):
    adj_cnt = 0 # 맞닿아 있는 변의 수
    num_a, num_b = arr[A[0][0]][A[0][1]], arr[B[0][0]][B[0][1]]

    for ax, ay in A:
        for dir in range(4):
            n_ax, n_ay = ax + dxs[dir], ay + dys[dir]
            if in_range(n_ax, n_ay) and (n_ax, n_ay) in B:
                adj_cnt += 1
    result = (len(A) + len(B))*num_a*num_b*adj_cnt
    return result

def rotate_arr():
    global arr
    hor, ver = n // 2, n//2
    new_arr = [[0]*n for _ in range(n)]
    nn = n//2
    
    for i in range(0, hor):
        for j in range(0, ver): # (0,0) -> (1, 1)
            ri, rj = j, nn-i-1
            new_arr[ri][rj] = arr[i][j]
    for i in range(hor): # (0,3) --> (1,4)
        for j in range(ver+1, n):
            oi, oj = i, j - ver - 1
            ri, rj = oj, nn-oi-1
            new_arr[ri][rj+ver+1] = arr[i][j]
    for i in range(hor+1, n):
        for j in range(ver):
            oi, oj = i-hor-1, j
            ri, rj = oj, nn - oi -1
            new_arr[ri+hor+1][rj] = arr[i][j]
    for i in range(hor+1, n):
        for j in range(ver+1, n):
            oi, oj = i - hor - 1, j -ver - 1
            ri, rj = oj, nn - oi - 1
            new_arr[ri+hor+1][rj+ver+1] = arr[i][j]
    


    # 십자가 -> 반시계
    middle = []
    for j in range(n):
        middle.append((hor, j))
        middle.append((j, ver)) 

    for i, j in middle:
        ri, rj = j, n - i - 1
        new_arr[i][j] = arr[ri][rj]

    arr = copy.deepcopy(new_arr)
    return 

for _ in range(4):
    groups = []
    visited = [[False]*n for _ in range(n)]
    find_group_pos()
    sum_grade = 0
    
    # 그룹 간의 조합 수
    combs = list(combinations([i for i in range(len(groups))], 2))

    for comb in combs:
        A, B = groups[comb[0]], groups[comb[1]]
        sum_grade += get_art_grade(A, B) # 각 각은 그룹의 위치를 나타냄 
    answer += sum_grade
    # print(sum_grade)
    # 회전 
    rotate_arr() 
print(answer)