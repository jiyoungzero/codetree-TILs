import sys
input =sys.stdin.readline


DIR_NUM = 4
WALL = '#'
BLANK = '.'
n = int(input())
cur_x, cur_y = tuple(map(int, input().split()))
arr = [[0]*(n+1) for _ in range(n+1)] 
for i in range(1, n+1):
    given_row = input().rstrip()
    for j, ele in enumerate(given_row):
        arr[i][j+1] = ele

visited = [[[False]*DIR_NUM for _ in range(n+1)] for _ in range(n+1)] # 탈출 가능 여부
answer = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 시계방향 
cur_dir = 0

def in_range(x, y):
    return 1 <= x < n and 1<= y < n  

def wall_exist(x, y):
    return in_range(x, y) and arr[x][y] == WALL

def simulate():
    global cur_x, cur_y, cur_dir, answer
    if visited[cur_x][cur_y][cur_dir]:
        print(-1)
        sys.exit(0)
    visited[cur_x][cur_y][cur_dir] = True

    nx, ny = cur_x+dxs[cur_dir], cur_y + dys[cur_dir]
    
    # case1 : 바라보는 방향으로 전진이 불가능한 경우
    if wall_exist(nx, ny):
        cur_dir = (cur_dir+3)%4
    # case2 : 바라보는 방향으로 전진이 가능한 경우 + 탈출
    elif not in_range(nx, ny):
        cur_x, cur_y = nx, ny # 탈출
        answer += 1 

    # case3: 바라보는 방향으로 전진이 가능한 경우
    else:
        check_dir = (cur_dir+1)%4
        # 앞으로 한 칸 전진 후 벽 짚은 곳
        check_x, check_y = nx + dxs[check_dir], ny+dys[check_dir]
        # 아래에 벽에 있고 전진이 가능한 경우
        if wall_exist(check_x, check_y):
            answer += 1
            cur_x, cur_y = nx, ny

        # 아래에 벽이 없고 시계방향 회전이 필요한 경우 :  두칸 이동 후 방향 회전
        else:
            cur_x, cur_y = check_x, check_y
            cur_dir = (cur_dir+1)%4
            answer += 2
    

while in_range(cur_x, cur_y): # 격자 빠져나오기 전까지 반복
    simulate()
print(answer)