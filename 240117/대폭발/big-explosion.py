import sys
input = sys.stdin.readline 


n, m, sr, sc = map(int, input().split())
sr -= 1
sc -= 1
arr = [[0]*n for _ in range(n)]
arr[sr][sc] = 1 

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
bomb_pos = []
answer, t = 0, 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def count_bomb():
    global answer 
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                answer += 1

def get_bomb_pos():
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                result.append((i, j))
    return result

def simulate(t):
    # 폭탄 위치 받기 
    bomb_pos = get_bomb_pos()

    # (t-1)초 폭탄은 2**(t-1)거리에 있는 곳에 폭탄을 둠
    for pos in bomb_pos:
        bx, by = pos
        for k in range(4):
            nxt_bx, nxt_by = bx + 2**(t-1)*dxs[k], by + 2**(t-1)*dys[k]
            if not in_range(nxt_bx, nxt_by):
                continue
            else:
                arr[nxt_bx][nxt_by] = 1



while t < m:
    t += 1
    simulate(t)
    

count_bomb()
print(answer)