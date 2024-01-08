import sys
input = sys.stdin.readline


dxs, dys = [-1,1,0,0],[0,0,-1,1]

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt_arr = [[0]*n for _ in range(n)]
pos = []
for _ in range(m):
    r, c = map(int, input().split())
    pos.append((r-1, c-1))

def in_range(x, y):
    if x < 0 or y < 0 or n <= x or n <= y:
        return False
    return True
    

def move(nxtcnt_arr):
    global cnt_arr, pos
    nxt_pos = []
    for r, c in pos:
        fr, fc = -1, -1
        for k in range(4):
            nr, nc = r+dxs[k], c+dys[k]
            if not in_range(nr, nc):continue

            if in_range(nr, nc):
                if (fr, fc) == (-1, -1):
                    fr, fc = nr, nc
                elif arr[fr][fc] < arr[nr][nc]:
                    fr, fc = nr, nc
                else:
                    continue
        nxtcnt_arr[fr][fc] += 1
        nxt_pos.append((fr, fc))

    cnt_arr = [row[:] for row in nxtcnt_arr]
    pos = nxt_pos
    return 


def find_collision():
    global cnt_arr
    for i in range(n):
        for j in range(n):
            if cnt_arr[i][j] > 1:
                cnt_arr[i][j] = 0
             


for _ in range(t):
    # 이동할 수 있는 곳 찾기
    # nxtcnt_arr에 이동한 곳에 구슬 개수 넣기   
    nxtcnt_arr = [[0]*n for _ in range(n)]
    move(nxtcnt_arr) 

    # cnt_arr에서 1이상인 곳 0으로 만들기
    find_collision()


answer = 0
for i in range(n):
    answer += cnt_arr[i].count(1)
print(answer)