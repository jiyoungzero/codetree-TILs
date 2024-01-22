import sys
input = sys.stdin.readline 

n, m, t, k = map(int, input().split())
balls = []
mapper_str_to_num = {"U": 0, "R": 1, "D": 2, "L": 3}
mapper_num_to_str = {0: 'U', 1: "R", 2:"D", 3:'L'}
direction = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
result_arr = []

for idx in range(m):
    r, c, d, v = map(str, input().split())
    r = int(r)-1
    c = int(c)-1
    balls.append([True, idx, r, c, d, int(v)])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def count_balls():
    result = 0
    for ball in balls:
        if ball[0]:
            result += 1
    return result

def move(target):
    flag, idx, r, c, d, v = target
    if not flag:
        return
    cur_dir = mapper_str_to_num[d]
    for _ in range(v):
        nr, nc = r+direction[cur_dir][0], c + direction[cur_dir][1]
        if not in_range(nr, nc):
            cur_dir = (cur_dir+2)%4
            nr, nc = r + direction[cur_dir][0], c + direction[cur_dir][1]
        r, c = nr, nc
    # 위치 업데이트
    balls[idx] = [True, idx, r, c, mapper_num_to_str[cur_dir], v] 
    

def bomb():
    cnt_arr = [[[] for _ in range(n)] for _ in range(n)]
    for ball in balls:
        flag, idx, r, c, d, v = ball
        if flag:cnt_arr[r][c].append((v, idx))
    
    for r in range(n):
        for c in range(n):
            length = len(cnt_arr[r][c])
            if length > k:
                cnt_arr[r][c].sort(key=lambda x:(-x[0], -x[1]))
                # 폭발된 것 -> false
                for i in range(k, length):
                    del_v, del_idx = cnt_arr[r][c][i]
                    balls[del_idx][0] = False
    return
            
            
def simulate():
    for ball in balls:
        move(ball)
    # print(balls)
    bomb()

while t > 0:
    simulate()
    t -= 1

print(count_balls())