import sys
input = sys.stdin.readline
from collections import defaultdict


dxs, dys = [-1,1,0,0],[0,0,-1,1]

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt_arr = [[0]*n for _ in range(n)]
pos = defaultdict(int)
for _ in range(m):
    r, c = map(int, input().split())
    pos[(r-1, c-1)] += 1

def in_range(x, y):
    if x < 0 or y < 0 or n <= x or n <= y:
        return False
    return True
    

def move(nxtcnt_arr):
    global cnt_arr, pos
    nxt_pos = defaultdict(int)
    for (r, c), nums in pos.items():
        fr, fc = int(1e9), int(1e9)
        for k in range(4):
            nr, nc = r+dxs[k], c+dys[k]
            if not in_range(nr, nc):continue

            if in_range(nr, nc):
                if (fr, fc) == (int(1e9), int(1e9)):
                    fr, fc = nr, nc
                elif arr[fr][fc] < arr[nr][nc]:
                    fr, fc = nr, nc
                else:
                    continue
        nxtcnt_arr[fr][fc] += 1
        nxt_pos[(fr, fc)] += 1

    cnt_arr = [row[:] for row in nxtcnt_arr]
    pos = nxt_pos
    return 


def find_collision():
    global cnt_arr
    global pos
    for i in range(n):
        for j in range(n):
            if cnt_arr[i][j] > 1:
                cnt_arr[i][j] = 0
                del pos[(i, j)]
             


for _ in range(t):
    # 이동할 수 있는 곳 찾기
    # nxtcnt_arr에 이동한 곳에 구슬 개수 넣기   
    nxtcnt_arr = [[0]*n for _ in range(n)]
    move(nxtcnt_arr) 

    # cnt_arr에서 1이상인 곳 0으로 만들기
    find_collision()

    # for i in range(n):
    #     print(nxtcnt_arr[i])
    # print()

    # print("충돌 후")
    
    # for i in range(n):
    #     print(cnt_arr[i])
    # print()
    # print(pos)



answer = 0
for i in range(n):
    answer += cnt_arr[i].count(1)
print(answer)