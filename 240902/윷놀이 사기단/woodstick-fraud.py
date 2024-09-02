import sys
input = sys.stdin.readline 


ARRIVED_HORSE = (-2, -2)

turns = list(map(int ,input().split()))
answer = 0

routes = [[i for i in range(0, 41, 2)] , # 제일 긴 루트
    [10, 13, 16, 19, 25, 30, 35, 40], # 10에서 멈췄을 때
    [20, 22, 24, 25, 30, 35, 40], # 20에서 멈췄을 때
    [30, 28, 27, 26, 25, 30, 35, 40]] # 30에서 멈췄을 때
answer = 0
horses = [(0, 0)]*4 # routes의 idx, 해당 루트에서의 idx

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def can_move(h_idx, moves): # 해당 위치에 다른 말이 없으며, 이미 h_idx가 arrived한 말이 아니라면 가능
    global horses
    if horses[h_idx] == ARRIVED_HORSE: return False

    prev_horses = deep_copy(horses)
    move(h_idx, moves)
    for i in range(4):
        if horses[i] == ARRIVED_HORSE or horses[i] == (0, 0):continue
        if h_idx != i and horses[h_idx] == horses[i]: 
            horses = deep_copy(prev_horses)
            return False
    horses = deep_copy(prev_horses)
    return True

def move(h_idx, moves):
    global horses
    r_idx, x = horses[h_idx]
    nx = x + moves

    # 현재 가장 긴 루트 일 때
    if r_idx == 0:
        # 격자 밖일 때
        if len(routes[r_idx]) <= nx:
            horses[h_idx] = ARRIVED_HORSE
            return 0
        # 10을 만났을 때
        if routes[r_idx][nx] == 10:
            horses[h_idx] = [1, 0]
            return 10
        # 20을 만났을 때
        elif routes[r_idx][nx] == 20:
            horses[h_idx] = [2, 0]
            return 20
        # 30을 만났을 때
        elif routes[r_idx][nx] == 30:
            horses[h_idx] = [3, 0]
            return 30
        # 그 외일 때 : 그대로 cur만 증가
        else: 
            horses[h_idx] = [0, nx]
            return routes[0][nx]
            
    
    # 10, 20, 30 중 하나를 만난 루트 일 때
    else:
        # 격자 밖일 때
        if len(routes[r_idx]) <= nx:
            horses[h_idx] = ARRIVED_HORSE
            return 0
        # 아닐 때
        else:
            horses[h_idx] = [r_idx, nx]
            return routes[r_idx][nx]


def backtracking(depth, score):
    global horses, answer
    if depth == 10:
        answer = max(answer, score)
        return

    for i in range(4):
        if not can_move(i, turns[depth]): continue
        prev_horses = deep_copy(horses)

        plus = move(i, turns[depth])
        backtracking(depth+1, score + plus)

        horses = deep_copy(prev_horses)

backtracking(0, 0)
print(answer)