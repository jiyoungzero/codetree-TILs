import sys
input = sys.stdin.readline 

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [1,-1,0,0], [0,0,1,-1]
people = []
for _ in range(m):
    a, b = map(int, input().split())
    people.append([a-1, b-1])
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
arrived = [False]*m
answer = 0
arr[ex][ey] = -1 # 출구


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def people_move():
    global people, answer, arrived
    nxt_people = []
    # print("현재 출구 위치 =", [ex, ey])
    for i, person in enumerate(people):
        if arrived[i]:
            nxt_people.append(person)
            continue
        moved = False
        x, y = person
        tmp = []
        now_dist = abs(x - ex) + abs(y - ey)
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny): continue
            if arr[nx][ny] > 0 : continue

            nxt_dist = abs(nx-ex) + abs(ny - ey)
            # print([x, y], "->", [nx, ny], ": ", now_dist, "에서",nxt_dist,"로 변화")
            if nx == ex and ny == ey: # 출구에 도착할 경우
                arrived[i] = True
                moved = True
                break 
            
            if now_dist > nxt_dist:
                moved = True
                tmp.append([nx, ny])

        if moved:answer += 1
        if not arrived[i] and len(tmp): # 출구에 도착하지 못한 애들만 업데이트
            nxt_people.append(tmp[0])
        elif arrived[i] or len(tmp) == 0: # 출구에 도착햇거나, 움직이지 못하는 경우
            nxt_people.append(person)
    people = nxt_people[:]

def possible_persion(x, y):
    for i, person in enumerate(people):
        if person == [x, y] and not arrived[i]:
            return True
    return False

def check(sx, sy, size): # 출구와 참가자 모두 있는지
    p_cnt = 0
    exit_flag = False
    for i in range(sx, sx+size):
        for j in range(sy, sy+size):
            if possible_persion(i, j):p_cnt += 1
            elif arr[i][j] == -1: exit_flag = True
    return exit_flag and p_cnt 

def find_square():
    flag = False
    square = []
    for size in range(2, n+1):
        for x in range(n-size+1): 
            for y in range(n-size+1):
                if check(x, y, size):
                    flag = True
                    square = [x, y, size]
                    break
            if flag:break
        if flag:break
    return square

def idx_rotate_person(x, y, rx, ry):
    global people
    result = []
    for i, person in enumerate(people):
        if not arrived[i] and [x, y] == person:
            result.append(i)
    return result

def deepcopy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def maze_rotate():
    global arr, ex, ey, people
    sx, sy, size = find_square()
    n_arr = deepcopy(arr)
    n_people = people[:]

    for x in range(sx, sx+size):
        for y in range(sy, sy+size):
            ox, oy = x-sx, y-sy
            rx, ry = oy, size-ox-1
            f_rx, f_ry = rx + sx, ry + sy

            if [x, y] in people:
                lst = idx_rotate_person(x, y, f_rx, f_ry)
                for idx in lst:
                    n_people[idx] = [f_rx, f_ry]

            n_arr[f_rx][f_ry] = arr[x][y]
            if n_arr[f_rx][f_ry] > 0:
                n_arr[f_rx][f_ry] -= 1
            elif n_arr[f_rx][f_ry] == -1: 
                ex, ey = f_rx, f_ry
        
    people = n_people[:]
    arr = deepcopy(n_arr)

            
def all_arrived():
    return all(arrived)

for time in range(k):
    if all_arrived():break
    
    people_move()
    if all_arrived():break
    # print("move후 = ", people)
    maze_rotate()
    # print("rotate 후 = ", people)
    # print(time+1, "출구 = ", [ex, ey])
    # print(time+1,"people =", people)
    
print(answer)
print(ex+1, ey+1)