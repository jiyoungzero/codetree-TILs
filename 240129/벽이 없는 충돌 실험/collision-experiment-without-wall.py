# 충돌
 # 중간에 충돌하는 것도 반영하기 위하여 x, y위치는 2배로 잡는다.
# 시간 
BLANK = -1
import sys
input = sys.stdin.readline 

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3  
}
balls = []
nxt_balls = []
dup_arr = [[-1]*4001 for _ in range(4001)]
cur_time = 0
answer = -1

def in_range(x, y):
    return 0 <= x < 4001 and 0 <= y < 4001

def move(ball):
    x, y, w, d, idx = ball
    nx, ny = x +dxs[d], y+dys[d]
    return (nx, ny, w, d, idx)

def collide(ball1, ball2):
    x1, y1, w1, d1, idx1 = ball1
    x2, y2, w2, d2, idx2 = ball2
    if w1 > w2 or (w1 == w2 and idx1 > idx2):
        return ball1
    else:
        return ball2

def push_nxt_balls(nxt_ball):
    global answer, dup_arr
    nx, ny, w, d, idx = nxt_ball

    if not in_range(nx, ny):
        return # 무시
    original_ball_idx = dup_arr[nx][ny]
    if original_ball_idx == BLANK:
        nxt_balls.append((nx, ny, w, d, idx))
        dup_arr[nx][ny] = len(nxt_balls) - 1
    else:
        target = collide(nxt_balls[original_ball_idx], nxt_ball)
        tx, ty, tw, td, tidx = target
        nxt_balls[original_ball_idx] = target
        dup_arr[tx][ty] = tidx
        answer = cur_time


def simulate():
    global balls, nxt_balls
    for ball in balls:
        nxt_ball = move(ball)
        push_nxt_balls(nxt_ball)
    
    balls = nxt_balls[:]
    for x, y, _, _, _ in nxt_balls:
        dup_arr[x][y] = BLANK
    nxt_balls = []

t = int(input())
for _ in range(t):
    n = int(input())
    balls = []
    for idx in range(n):
        x, y, w, d = map(str, input().split())
        x = int(x)*2 + 2000
        y = int(y)*2 + 2000
        w = int(w)
        balls.append((x, y, w, mapper[d], idx))
    
    for i in range(1, 4001):
        cur_time = i
        simulate()
    print(answer)