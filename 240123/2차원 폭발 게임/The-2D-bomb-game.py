import sys
input = sys.stdin.readline 


n, m , k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate_90():
    global arr
    rotate_grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_grid[j][n-i-1] = arr[i][j]
    arr = [row for row in rotate_grid]
    return

def get_end_idx(col, start_idx, target):
    for end_idx in range(start_idx+1, n):
        if arr[end_idx][col] != target:
            return end_idx - 1
    return (n-1)

def bomb():
    
    while True:
        flag = False
        for col in range(n):
            cnt = 1
            for cur_row in range(n):
                target = arr[cur_row][col]
                if target > 0:
                    end_idx = get_end_idx(col, cur_row, target)
                    if end_idx-cur_row+1 >= m:
                        for i in range(cur_row, end_idx+1):
                            flag = True
                            arr[i][col] = 0
        gravity()
        if not flag:
            break
                        
    return 

def gravity():
    global arr
    nxt_arr = [[0]*n for _ in range(n)]
    for col in range(n):
        tmp_row = (n-1)
        for row in range(n-1, -1, -1):
            if arr[row][col]:
                nxt_arr[tmp_row][col] = arr[row][col]
                tmp_row -= 1
    arr = [row for row in nxt_arr]

def count_bomb():
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                result += 1
    return result



while k >= 0:
    bomb()
    rotate_90()
    gravity()
    k -= 1


# while bomb_flag:
#     bomb_flag = bomb()
#     gravity()
#     rotate_90()
#     gravity()

print(count_bomb())