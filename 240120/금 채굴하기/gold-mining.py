import sys
input = sys.stdin.readline
from collections import deque

GOLD = 1
BLANK = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
answer = 0


def in_range(x, y):
    return 0 <= x <n and 0 <= y < n

def get_gold_for_k(k, x, y):
    gold_value = 0
    que = deque()
    que.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    if arr[x][y] == GOLD:
        gold_value += m 
    
    # k == 0인 경우
    if k == 0:return gold_value
        
    time = get_findcost(k)
    for _ in range(time):
        cur_x, cur_y = que.popleft()

        for d in range(4):
            nx, ny = cur_x+dxs[d], cur_y+dys[d]
            if in_range(nx, ny) and not visited[nx][ny]:
                if arr[nx][ny] == GOLD:
                    gold_value += m 
                visited[nx][ny] = True
            que.append((nx, ny))
 
    return gold_value
        


def get_findcost(k):
    return k*k+(k+1)*(k+1)

for i in range(n):
    for j in range(n):
        for size in range(n+1):
            gold_value = get_gold_for_k(size, i, j)
            gold_cnt = gold_value//m
            if answer < gold_cnt and get_findcost(size) <= gold_value:
                answer = gold_cnt
                

print(answer)