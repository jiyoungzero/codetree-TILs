BLANK = -1

t = int(input())
n = 0
marbles = []
nxt_marbles = []
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
nxt_arr = [
    [BLANK for _ in range(4001)]
    for _ in range(4001)
]

cur_time = 0
last_collision_time = -1

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3  
}

def in_range(x, y):
    return 0 <= x < 4001 and 0 <= y < 4001

def move(marble):
    global last_collision_time
    x, y, w, d, i = marble 
    nx,ny = x + dxs[d], y+dys[d]
    return (nx, ny, w, d, i)

def collide(marble1, marble2):
    if (marble1[2] > marble2[2]) or (marble1[2] == marble2[2] and marble1[4] > marble2[4]):
        return marble1
    else:
        return marble2

def push_next_marble(marble):
    global last_collision_time
    x, y, w, d, i = marble
    if not in_range(x, y):
        return 
    
    original_marble_idx = nxt_arr[x][y]
    if original_marble_idx == BLANK:
        nxt_marbles.append(marble)
        nxt_arr[x][y] = len(nxt_marbles) - 1
    else:
        nxt_marbles[original_marble_idx] = collide(nxt_marbles[original_marble_idx], marble)
        last_collision_time = cur_time

def simulate():
    global marbles, nxt_marbles
    nxt_marbles = []
    for x, y, _, _, _ in nxt_marbles:
        nxt_arr[x][y] = BLANK

    for marble in marbles:
        nxt_marble = move(marble)
        push_next_marble(nxt_marble)

    marbles = nxt_marbles[:]

for _ in range(t):
    marbles = []
    last_collision_time = -1

    n = int(input())
    for i in range(1, n+1):
        x, y, w, d = map(str, input().split())
        x, y, w = int(x), int(y), int(w)
        # 중간에 충돌하는 경우를 깔끔하게 하기 위해 
        x = x * 2
        y = y * 2
        marbles.append([x+2000, y+2000, w, mapper[d], i])

    for i in range(1, 4001):
        cur_time = i
        simulate()
    print(last_collision_time)