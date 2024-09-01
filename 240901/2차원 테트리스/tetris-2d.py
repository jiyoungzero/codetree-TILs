import sys
input = sys.stdin.readline 


# 만약 행이나 열이 타일로 가득찬 경우와 연한칸에 타일이 있는 경우가 동시에 발생 :
# 1)  타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 
# 2) 연한 칸에 블록이 있는 경우를 처리
k = int(input())
cmds = [tuple(map(int, input().split())) for _ in range(k)]
types = [[(0,0)], [(0,0), (0, 1)], [(0, 0), (1, 0)]]

yellow_score = 0
red_score = 0

# red쪽으로 갈 때 : x는 그대로, y좌표만 오른쪽으로
# yellow쪽으로 갈 때 : y는 그대로, x좌표만 아래쪽으로 

red = [[0]*10 for _ in range(4)]
yellow = [[0]*4 for _ in range(10)]

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def red_full():
    remove_col = []
    for col in range(9, 3, -1):
        flag = True
        for row in range(4): 
            if red[row][col] == 0:
                flag = False
                break 
        if flag: 
            remove_col.append(col)
    return remove_col

def red_remove(r_lst):
    global red 
    tmp_col = 9
    nxt_red = [[0]*10 for _ in range(4)]
    n_col = 9
    for col in range(9, 3, -1):
        if col in r_lst:
            tmp_col -= 1
        else:
            for row in range(4):
                nxt_red[row][n_col] = red[row][tmp_col] 
            tmp_col -= 1
            n_col -= 1
    red = deep_copy(nxt_red)

def yellow_remove(r_lst):
    global yellow 
    tmp_row = 9
    nxt_yellow = [[0]*4 for _ in range(10)]
    n_row = 9
    for row in range(9, 3, -1):
        if row in r_lst:
            tmp_row -= 1
        else:
            for col in range(4):
                nxt_yellow[n_row][col] = yellow[tmp_row][col] 
            tmp_row -= 1
            n_row -= 1
    yellow = deep_copy(nxt_yellow)

def yellow_full():
    remove_row = []
    for row in range(9, 3, -1):
        flag = True
        for col in range(4): 
            if yellow[row][col] == 0:
                flag = False
                break 
        if flag: 
            remove_row.append(row)
    return remove_row 

def red_zone(): # 연한 칸에 타일이 잇는 경우
    global red
    lift_cnt = 0
    for col in range(4,6):
        for row in range(4):
            if red[row][col] == 1:
                lift_cnt += 1
                break 
    nxt_red = []
    for row in range(4):
        new = [0]*lift_cnt + red[row][:10-lift_cnt]
        nxt_red.append(new)
    red = deep_copy(nxt_red)

def yellow_zone():
    global yellow
    lift_cnt = 0
    for row in range(4,6):
        for col in range(4):
            if yellow[row][col] == 1:
                lift_cnt += 1
                break 
    nxt_yellow = [[0]*4 for _ in range(10)] 
    for col in range(4):
        new = [0]*lift_cnt
        for row in range(0, 10-lift_cnt):
            new.append(yellow[row][col])
        for i in range(10):
            nxt_yellow[i][col] = new[i]
    yellow = deep_copy(nxt_yellow)
    

def move2red(t, x, y): # x는 그대로, y좌표만 구하기
    global red_score
    if t == 0 or t == 1:
        min_col = 4
        for col in range(4, 9):
            if red[x][col+1] == 1: break
            else: min_col += 1
        if t == 0: red[x][min_col] = 1
        else: red[x][min_col], red[x][min_col-1] = 1, 1
    elif t == 2:
        min_col = 9
        for tx in [x, x+1]:
            for col in range(4, 10):
                if red[tx][col] == 1:
                    min_col = min(min_col, col-1)
                    break 
        red[x][min_col], red[x+1][min_col] = 1, 1
    
    while True:
        r_lst = red_full()
        if len(r_lst) > 0:
            red_remove(r_lst)
            red_score += len(r_lst)
        else: break
    red_zone()
        
def move2yellow(t, x, y):
    global yellow_score
    if t == 0 or t == 2:
        min_row = 4
        for row in range(4, 9):
            if yellow[row+1][y] == 1: break
            else: min_row += 1
        if t == 0: yellow[min_row][y] = 1
        else:
            yellow[min_row][y], yellow[min_row-1][y] = 1, 1
    elif t == 1:
        min_row = 9
        for ty in [y, y+1]:
            for row in range(4, 10):
                if yellow[row][ty] == 1: 
                    min_row = min(min_row, row-1)
                    break
        yellow[min_row][y], yellow[min_row][y+1] = 1, 1
    

    while True:
        r_lst = yellow_full()
        if len(r_lst) > 0:
            yellow_remove(r_lst)
            yellow_score += len(r_lst)
        else: break
    yellow_zone()


# red = [[0]*10 for _ in range(4)]
# red[0][6], red[1][6], red[1][7], red[1][8], red[1][9], red[3][9] = 1,1,1,1,1,1
# red[1][5] = 1
# red[1][4] = 1
# for row in red:
#     print(*row)   
# print()
# red_zone()
# for row in red:
#     print(*row)   

# yellow = [[0]*4 for _ in range(10)]
# yellow[6][2], yellow[7][0], yellow[7][1], yellow[7][2], yellow[7][3] = 1, 1, 1, 1, 1
# yellow[8][1], yellow[9][1], yellow[8][3], yellow[9][3] = 1, 1, 1, 1
# yellow[5][2] = 1
# yellow_zone()
# # r_lst = yellow_full()
# # yellow_remove(r_lst)
# for row in yellow:
#     print(*row)   
# print()

def get_remain(arr):
    row, col = len(arr), len(arr[0])
    cnt = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                cnt += 1
    return cnt
                

for t, x, y in cmds:
    t -= 1
    move2red(t, x, y)
    move2yellow(t, x, y)

print(yellow_score+red_score)
print(get_remain(red) + get_remain(yellow))