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

def bomb():
    erase_info = [] # (열, start_row, end_row)
    for col in range(n):
        cnt = 1
        row = 0
        if cnt == m and len(arr) == 1:
            erase_info.append((col, 0, 1))
        while row < n:
            target = arr[row][col]
            nxt_row = row+1
            while nxt_row < n:
                if target == arr[nxt_row][col]:
                    cnt += 1                    
                    if nxt_row == (n-1) and cnt >= m:
                        erase_info.append((col, row, nxt_row+1))
                    nxt_row += 1

                else:
                    if cnt >= m:
                        erase_info.append((col, row, nxt_row))
                    cnt = 1
                    break
            row = nxt_row
            

    for erase in erase_info:
        col, start_row, end_row = erase
        for i in range(start_row, end_row):
            arr[i][col] = 0
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
    gravity()
    rotate_90()
    gravity()
    k -= 1

print(count_bomb())