import sys
input = sys.stdin.readline 
import copy

HUMAN = -1
EXIT = -2

# 원인 -> 회전 할 때, people의 위치를 업데이트 하지 않음 
dxs, dys = [-1,1,0,0], [0,0,1,-1]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
people_board = [[[] for _ in range(N)] for _ in range(N)]
people = []
answer = 0 # 총 이동위치 
for idx in range(M):
    x, y = map(int, input().split())
    people.append((x-1, y-1, False)) # 탈출 여부 
    people_board[x-1][y-1].append(idx+1)
exit_x, exit_y = tuple(map(int, input().split())) # 출구 위치 
board[exit_x-1][exit_y-1] = EXIT 


def rotate_arr_90(arr):
    rotated_arr = list(map(list, zip(*arr[::-1])))
    return rotated_arr

def print_arr(arr):
    for row in arr:
        print(*row)
    print()

def game_over():
    for person in people:
        if not person[-1]:
            return False
    return True 

def all_move():
    global board, answer
    nxt_board = [[0]*N for _ in range(N)]
    nxt_people_board = [[[] for _ in range(N)] for _ in range(N)]
    now_exit = (0,0)
    for row in range(N):
        for col in range(N):
            if board[row][col] != HUMAN:
                nxt_board[row][col] = board[row][col]
            if board[row][col] == EXIT:
                now_exit = (row, col)
                nxt_board[row][col] = EXIT

    
    for i, person in enumerate(people):
        sx, sy, escape = person
        if not escape:
            s_dist = abs(now_exit[0] - sx) + abs(now_exit[1] - sy)
            possible = [] # (출구까지의 거리, 이동방향 )

            for dir in range(4):
                nx, ny = sx + dxs[dir], sy + dys[dir]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] <= 0:
                    cur_dist = abs(now_exit[0]-nx) + abs(now_exit[1] - ny)
                    if cur_dist < s_dist:
                        possible.append((cur_dist, dir, nx, ny))
            if len(possible) == 0: # 움직일 수 없다면 
                # 원래 위치 그대로
                nxt_board[sx][sy] = HUMAN
                nxt_people_board[sx][sy].append(i+1)
            else:
                possible.sort(key = lambda x:(x[0], x[1]))
                final_x, final_y = possible[0][2], possible[0][3]

                # 이동
                answer += 1

                # 탈출 했으면
                if nxt_board[final_x][final_y] == EXIT:
                    print_arr(nxt_board)
                    people[i] = (final_x, final_y, True)
                # 탈출 안했으면 
                else:
                    nxt_board[final_x][final_y] = HUMAN
                    nxt_people_board[sx][sy].append(i+1)
                    people[i] = (final_x, final_y, False)

    board = copy.deepcopy(nxt_board)
    people_board = copy.deepcopy(nxt_people_board)
    return 

def find_smallest_maze():
    for s in range(2, N+1):
        # size = s*s # 가장 작은 미로의 크기
        for row in range(N-s+1): 
            for col in range(N-s+1):
                person_cnt, exit_cnt = 0,0
                for i in range(row, row+s):
                    for j in range(col, col+s):
                        if len(people_board[i][j]) > 0:person_cnt += 1
                        if board[i][j] == EXIT: exit_cnt += 1
                        
                        if person_cnt >= 1 and exit_cnt == 1:
                            return (row, col, s) # 좌측 상단 정사각형 시작 위치, 크기의 한 변

def rotate_maze():
    global board
    h, c, arr_len = find_smallest_maze()
    # 회전할 정사각형 부분 
    target_arr = []
    ppl_arr = []
    for i in range(h, h+arr_len):
        tmp = []
        tmp_ppl = []
        for j in range(c, c+arr_len):
            if board[i][j] > 0:
                board[i][j] -= 1 # 벽이라면 내구성 1감소
            tmp_ppl.append(people_board[i][j])
            tmp.append(board[i][j])
        target_arr.append(tmp)
        ppl_arr.append(tmp_ppl)
    target_arr = rotate_arr_90(target_arr)
    ppl_arr = rotate_arr_90(ppl_arr)
    print(ppl_arr)
    # 원래의 board에 끼우기 
    for i in range(h, h+arr_len):
        for j in range(c, c+arr_len):
            board[i][j] = target_arr[i-arr_len][j-arr_len]
            people_board[i][j].append(ppl_arr[i-arr_len][j-arr_len])

    # 회전한 ppl_arr를 기반하여 people 정보 업데이트
    for i in range(N):
        for j in range(N):
            if len(people_board[i][j]) > 0:
                for idx in people_board[i][j]:
                    print(people_board[i][j])
                    people[idx-1] = (i, j, False)

    

for k in range(K):
    if game_over():
        break
    all_move()

    rotate_maze()

print(answer)