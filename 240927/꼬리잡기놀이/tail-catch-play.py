import sys
input = sys.stdin.readline 
from collections import deque

HEAD = 1
REST = 2
TAIL = 3
ROAD = 4
BLANK = 0

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
cur_team = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def go_forward(x, y):
    dxs, dys = [0,0,1,-1],[1,-1,0,0]
    # (x, y)를 헤드로 하는 팀의 모든 위치 받기
    team = [(x, y)] # 0번째 : 헤드, -1번째 : 꼬리
    more_than_two = False
    # 팀이 2명인 경우
    for dir in range(4):
        nx, ny = x + dxs[dir], y + dys[dir]
        if in_range(nx, ny) and arr[nx][ny] == 2: 
            more_than_two = True
            
    que = deque()
    que.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True 
    
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if not visited[nx][ny] and arr[nx][ny] != BLANK and arr[nx][ny] != ROAD:
                if more_than_two and arr[x][y] == HEAD and arr[nx][ny] == 3:continue
                visited[nx][ny] = True 
                que.append((nx, ny))
                team.append((nx, ny))
    
    # 헤드만 이동시키기
    next_team = []
    x, y = team[0]
    for dir in range(4):
        nx, ny = x + dxs[dir], y + dys[dir]
        if in_range(nx, ny) and (arr[nx][ny] == ROAD or arr[nx][ny] == TAIL):
            next_team.append((nx, ny))
            break 
    next_team += team[:-1]
    # print(team , "--->", next_team)
    return (team, next_team)


def all_go_forward():
    global arr, cur_team
    prev_team = []
    nxt_team = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == HEAD:
                prev, nxt = go_forward(i, j)
                prev_team.append(prev)
                nxt_team.append(nxt)
    
    # 이전 team의 위치는 4로 만들고
    for team in prev_team:
        for i, j in team:
            arr[i][j] = ROAD

    # 이동 후의 위치 next_team을 arr에 다시 넣기
    for next_team in nxt_team:
        arr[next_team[0][0]][next_team[0][1]] = 1
        arr[next_team[-1][0]][next_team[-1][1]] = 3
        for i, j in next_team[1:-1]:
            arr[i][j] = 2

    cur_team = nxt_team[:]
    # print("---new ! ---")
    # for row in arr:
    #     print(*row)

def get_score(row, col):
    global answer, arr
    for team in cur_team:
        if (row, col) in team:
            for i in range(len(team)):
                if team[i] == (row, col):
                    answer += (i+1)**2
                    # 머리, 꼬리 위치 바뀜
                    h_pos = team[0]
                    t_pos = team[-1]
                    arr[t_pos[0]][t_pos[1]] = HEAD 
                    arr[h_pos[0]][h_pos[1]] = TAIL
                    # print("---get~! : ", (i+1)**2, "final_score : ", answer)
                    # print("---switch ! ---")
                    # for row in arr:
                    #     print(*row)
                    # print()
                    return 


def throw_ball(time):
    ball_side, ball_pos = time//n, time%n
    if ball_side == 0: # 오른쪽으로
        row = ball_pos 
        for col in range(n):
            if arr[row][col] != ROAD and arr[row][col] != BLANK:
                get_score(row, col)
                return 

    elif ball_side == 1: # 위로
        col = ball_pos
        for row in range(n-1, -1, -1):
            if arr[row][col] != ROAD and arr[row][col] != BLANK:
                get_score(row, col)
                return 

    elif ball_side == 2: # 왼쪽으로 
        row = n - 1 - ball_pos 
        for col in range(n-1, -1, -1):
            if arr[row][col] != ROAD and arr[row][col] != BLANK:
                get_score(row, col)
                return 

    else: # 아래로
        col = n - 1 - ball_pos 
        for row in range(n):
            if arr[row][col] != ROAD and arr[row][col] != BLANK:
                get_score(row, col)
                return 


# 1. 한칸 이동 
# 2. 공 발사
# 3. 점수 얻기 
for time in range(k):
    # print(time, "번 째")
    all_go_forward()
    throw_ball(time)

print(answer)