import sys
input = sys.stdin.readline 
from collections import deque

#  di | 0,1,2,3 : 북, 동, 남, 서쪽
R, C, K = map(int, input().split())
golams = []
for _ in range(K):
    ci, di = map(int ,input().split())
    golams.append((ci-1, di))
arr = [[0]*C for _ in range(R+3)]
answer = 0
g_idx = 1 
def can_down(sx, sy):
    return sx + 2 < R+3 and arr[sx+2][sy] == 0 and arr[sx+1][sy-1] == 0 and arr[sx+1][sy+1] == 0

def can_left_down(sx, sy):
    return 0 <= sy - 2 and sx + 2 < R+3 and arr[sx-1][sy-1] == 0 and arr[sx][sy-2] == 0 and arr[sx+1][sy-1] == 0 and arr[sx+1][sy-2] == 0 and arr[sx+2][sy-1] == 0

def can_right_down(sx, sy):
    return sx + 2 < R+3 and sy + 2 < C and arr[sx-1][sy+1] == 0 and arr[sx][sy+2] == 0 and arr[sx+1][sy+1] == 0 and arr[sx+1][sy+2] == 0 and arr[sx+2][sy+1] == 0

def down(ci, di):
    global arr, answer
    sx, sy = 1, ci
    # print(sx, sy, "start")
    while True:
        # print(sx, sy)
        if not (can_down(sx, sy) or can_left_down(sx, sy) or can_right_down(sx, sy)):
            break
    # 최대한 아래로 하강 
        while can_down(sx, sy):
            sx += 1
        
        # 서쪽 방향으로 하강 
        while can_left_down(sx, sy) :
            sx += 1
            sy -= 1
            # 출구 반시계방향으로 회전 
            di -= 1
            if di == -1:
                di = 3
        
        # 남쪽 방향으로 하강 
        while can_right_down(sx, sy):
            sx += 1
            sy += 1
            # 출구 시계방향 회전
            di = (di+1)%4 
    
    # 해당 위치에 골렘 위치 시키기
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    arr[sx][sy] = g_idx
    for dir in range(4):
        if dir == di:
            arr[sx+dxs[dir]][sy+dys[dir]] = -g_idx
        else:
            arr[sx+dxs[dir]][sy+dys[dir]] =  g_idx
    
    # 만약 sx-1 < 3 이면 arr 초기화
    if sx - 1 < 3:
        arr = [[0]*C for _ in range(R+3)]
        return 
    
    # 아니라면 출구를 타고 제일 아래로 내려가기 
    # 1) abs는 같은 곳은 갈 수 있음 
    # 2) -에서 +인 곳은 무조건 갈 수 있음 
    que = deque()
    que.append((sx, sy))
    visited = [[False]*C for _ in range(R+3)]
    visited[sx][sy] = True 
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if 0 <= nx < R+3 and 0 <= ny < C:
                if not visited[nx][ny]:
                    if abs(arr[x][y]) == abs(arr[nx][ny]) or (arr[x][y] < 0 and arr[nx][ny] != 0):
                        visited[nx][ny] = True 
                        que.append((nx, ny))
    # print(g_idx, "번째 골렘 이동 후")
    # for row in arr:
    #     print(*row)
    # print(g_idx, "번째 골렘이 갈 수 있는 곳")
    # for row in visited:
    #     print(*row)
    # print()
    for row in range(R+2, 2, -1):
        for col in range(C):
            if arr[row][col] != 0 and visited[row][col]:
                answer += (row - 2)
                # print(row-2)
                return 
            
    

while golams:
    ci, di = golams.pop(0)
    down(ci, di)
    g_idx += 1
print(answer)