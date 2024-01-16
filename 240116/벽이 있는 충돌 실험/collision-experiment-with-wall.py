import sys
input = sys.stdin.readline


T = int(input())
match_dir = {'U':(-1, 0), 'R':(0, 1), 'D':(1,0), 'L':(0,-1)}

def flip_dir(cur_dir):
    if cur_dir == 'U':
        return 'D'
    elif cur_dir == 'R':
        return 'L'
    elif cur_dir == 'L':
        return 'R'
    else:
        return "U"

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move(arr):
    n = len(arr)
    tmp_arr = [[0]*n for _ in range(n)]
    cnt_arr = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                cur_dir = match_dir[arr[i][j]]
                ni, nj = i + cur_dir[0],  j + cur_dir[1] 
                if not in_range(ni, nj):
                    # 방향 전환
                    tmp_arr[i][j] = flip_dir(arr[i][j])
                    cnt_arr[i][j] += 1                    
                else:
                    tmp_arr[ni][nj] = arr[i][j]
                    cnt_arr[ni][nj] += 1
    return (tmp_arr, cnt_arr)
                    
def del_collision_ball(nxt_arr, cnt_arr):
    n = len(nxt_arr)
    for i in range(n):
        for j in range(n):
            if cnt_arr[i][j] > 1:
                nxt_arr[i][j] = 0
    return nxt_arr

def count_ball(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                result += 1
    return result         

for _ in range(T):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]

    for _ in range(m):
        x, y , d = map(str, input().split())
        x, y = int(x), int(y)
        arr[x-1][y-1] = d

    for _ in range(n*2): # 충분히 오래 이동
        nxt_arr, cnt_arr = move(arr)
        arr = del_collision_ball(nxt_arr, cnt_arr)
    
    print(count_ball(arr))