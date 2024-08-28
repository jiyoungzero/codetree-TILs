import sys
input = sys.stdin.readline 

BLANK = 0
WALL = -1


n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
her_arr = [[0]*n for _ in range(n)]
#  단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 
# 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
# 제초제는 c년만큼 남아있다가 c+1일 때 빈칸으로 변함
r_dxs, r_dys = [-1, -1, 1, 1], [-1, 1, -1, 1] 
dxs, dys = [0,0, 1, -1], [1, -1, 0, 0]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def growing_trees():
    global arr
    nxt_arr = deep_copy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                up = 0
                for dir in range(4):
                    ni, nj = i + dxs[dir], j + dys[dir]
                    if not in_range(ni, nj):continue
                    if arr[ni][nj] > 0: up += 1
                nxt_arr[i][j] += up
    arr = deep_copy(nxt_arr)


def spreading_trees():
    global arr
    nxt_arr = deep_copy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and her_arr[i][j] == 0:
                cnt = 0
                for dir in range(4):
                    ni, nj = i + dxs[dir], j + dys[dir]
                    if not in_range(ni, nj): continue
                    if arr[ni][nj] == BLANK and her_arr[ni][nj] == 0: cnt += 1
                if cnt > 0:
                    child = arr[i][j] // cnt
                    for dir in range(4):
                        ni, nj = i + dxs[dir], j + dys[dir]
                        if not in_range(ni, nj): continue
                        if arr[ni][nj] == BLANK and her_arr[ni][nj] == 0: nxt_arr[ni][nj] += child
    arr = deep_copy(nxt_arr)

def find_place():
    global answer
    max_value = -1
    place = [0, 0]

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if arr[i][j] > 0 and her_arr[i][j] == 0:
                cnt = arr[i][j]
                for dir in range(4):
                    for dist in range(1, k+1):
                        ni, nj = i + r_dxs[dir]*dist, j + r_dys[dir]*dist
                        if not in_range(ni, nj) or her_arr[ni][nj] > 0: break
                        if arr[ni][nj] == WALL or arr[ni][nj] == 0:break
                        else:cnt += arr[ni][nj]
                if max_value <= cnt:
                    max_value = cnt
                    place = [i, j]
    answer += max_value
    # print(place, max_value)
    return place
                

def go_herbicide():
    global arr
    x, y = find_place()

    arr[x][y] = 0
    her_arr[x][y] = c+1
    # 제초제를 뿌리는 곳 찾기
    for dir in range(4):
        for dist in range(1, k+1):
            nx, ny = x + r_dxs[dir]*dist, y + r_dys[dir]*dist
            if not in_range(nx, ny):break
            if arr[nx][ny] == 0 or arr[nx][ny] == WALL:
                her_arr[nx][ny] = c+1
                break
            else:
                arr[nx][ny] = 0
                her_arr[nx][ny] = c+1
                
                
# def delete_past_herbicide():
#     global her_arr
#     for i in range(n):
#         for j in range(n):
#             if her_arr[i][j] == m:
#                 her_arr[i][j] = 0

def decreasing_herbicide():
    for i in range(n):
        for j in range(n):
            if her_arr[i][j]:
                her_arr[i][j] -= 1

while m:
    # for row in arr:
    #     print(*row)
    # print()   
    growing_trees()
    # print("after growing_trees")
    # for row in arr:
    #     print(*row)
    # print()
      
    spreading_trees()
    # print("after spreading_trees")
    # for row in arr:
    #     print(*row)
    # print()
    go_herbicide()
    decreasing_herbicide() 
    # print("after go_herbicide")
    # for row in arr:
    #     print(*row)
    # print()

    # print("her_arr")
    # for row in her_arr:
    #     print(*row)
    # print()
    m -= 1


print(answer)
# for row in arr:
#     print(*row)
# print()