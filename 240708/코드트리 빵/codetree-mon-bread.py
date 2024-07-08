import sys
input = sys.stdin.readline 
from collections import deque


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 0 : 빈칸, 1: 베이스캠프
stores = []
for _ in range(m):
    x, y = map(int, input().split())
    stores.append((x-1, y-1)) 

arrived = [False]*m # 원하는 편의점에 도착했는지 
ppl = {}
for i in range(m):
    ppl[i] = [] # 아직 격자 안에 없음 

dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0] # 위, 왼쪽, 오른쪽, 아래
answer = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 위치까지 가는데 최소거리 계산 
def bfs(store):
    que = deque()
    que.append(store)
    visited = [[-1]*n for _ in range(n)]
    visited[store[0]][store[1]] = 0

    result = []
    while que:
        x, y = que.popleft()
        if arr[x][y] == 1:
            result = [x, y]
            break
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if visited[nx][ny] == -1 and arr[nx][ny] != -1: # arr[x][y] == -1 : 갈 수 없는 곳
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
    return result

def move_p(key):
    global new_arrived
    x, y = ppl[key]
    target = stores[key]

    if target[0] < x:
        x -= 1
    elif target[1] < y:
        y -= 1
    elif target[1] > y:
        y += 1
    else:
        x += 1

    if target == (x, y):
        arrived[key] = True
        new_arrived.append(target)
    # 새로운 이동 위치 업데이트
    ppl[key] = [x, y]
    return 

new_arrived = []
while True:
    for key, p in ppl.items():
        if arrived[key]:continue
        if len(p):
            move_p(key) 
    # 격자 안 사람들 모두 이동 후, 편의점에 도착한 곳 == -1 처리
    for ax, ay in new_arrived:
        arr[ax][ay] = -1
    
    if answer <= m:
        base_pos = bfs(stores[answer-1]) # t분 일 때, t번째 사람이 가고자 하는 편의점과 가까운 베이스캠프 위치
        arr[base_pos[0]][base_pos[1]] = -1
        ppl[answer-1] = [base_pos[0], base_pos[1]]

    if all(arrived):break    
    # print(answer, ppl)
    answer += 1

print(answer)