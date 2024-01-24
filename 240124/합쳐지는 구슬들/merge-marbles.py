import sys
input = sys.stdin.readline

# 충돌시 무게는 합쳐지며 그 중 가장 큰 번호와 해당 번호의 방향을 따름

n, m , t = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
balls = []
mapper = {"U":0,"D":2 , "R":1, "L":3}
direction = { 0 : (-1, 0), 2:(1, 0), 1: (0, 1), 3:(0, -1)}
new_ball_idx = 0

for idx in range(m):
    r, c, d, w = map(str, input().split())
    r = int(r) - 1
    c = int(c) - 1
    balls.append((idx, r, c, mapper[d], int(w)))
    arr[r][c].append(idx) # 현재 해당 구슬 idx
    new_ball_idx = idx


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def arr_to_ball_index(idx):
    for i, ball in enumerate(balls):
        if ball[0] == idx:
            return i

def move():
    global arr
    for i, ball in enumerate(balls):
        idx, r, c, d, w = ball
        nr, nc = r+direction[d][0], c + direction[d][1]

        if not in_range(nr, nc):
            balls[i] = (idx, r, c, (d+2)%4, w)
            continue
        else:
            balls[i] = (idx, nr, nc, d, w)
            arr[r][c].remove(idx) # 해당 구슬 삭제
            arr[nr][nc].append(idx)

    return

def get_sum_weight(x, y):
    result = 0
    for idx in arr[x][y]:
        i = arr_to_ball_index(idx)
        result += balls[i][-1]
    return result

def get_max_dir_idx(x, y):
    max_dir, max_idx = 0, 0
    for idx in arr[x][y]:
        max_idx = max(max_idx, idx)

    for ball in balls:
        if ball[0] == max_idx:
            max_dir = ball[3]
            break
    return (max_dir, max_idx)

def collision():
    global arr, new_ball_idx
    for r in range(n):
        for c in range(n):
            if len(arr[r][c]) > 1:
                sum_weight = get_sum_weight(r, c)
                max_dir, max_idx = get_max_dir_idx(r, c)
                # 충돌한 구슬들 제거
                for del_idx in arr[r][c]:
                    for ball in balls:
                        if ball[0] == del_idx:
                            balls.remove(ball)
                arr[r][c] = []
                # 새롭게 합쳐진 구슬 추가
                new_ball_idx += 1
                balls.append((new_ball_idx, r, c, max_dir, sum_weight))
                arr[r][c].append(new_ball_idx)
    return 

def simulate():
    move()
    collision()

while t > 0 :
    t -= 1
    simulate()


balls.sort(key = lambda x:-x[4])
print(len(balls), balls[0][4])