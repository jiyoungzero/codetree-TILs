import sys
input = sys.stdin.readline 
from collections import deque

k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
fragments = deque(list(map(int, input().split())))
answer = 0 
dxs, dys = [0,0,1,-1], [-1, 1, 0,0]
def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def first_get_values(a): # 획득한 가치만 리턴 
    visited = [[False]*5 for _ in range(5)]
    first_value = 0

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                cnt = 1

                que = deque()
                que.append((i, j))
                visited[i][j] = True 
                while que:
                    x, y = que.popleft()
                    for dir in range(4):
                        nx, ny = x + dxs[dir], y + dys[dir]
                        if not in_range(nx, ny):
                            continue 
                        if not visited[nx][ny] and a[i][j] == a[nx][ny]:
                            cnt += 1
                            visited[nx][ny] = True 
                            que.append((nx, ny))
                if cnt >= 3: first_value += cnt 
    return first_value

def test_rotate_90(sx, sy, r_cnt):
    test_arr = deep_copy(arr)
    for _ in range(r_cnt):
        prev_arr = deep_copy(test_arr)
        for i in range(sx, sx+3):
            for j in range(sy, sy+3):
                oi, oj = i-sx, j-sy 
                ri, rj = oj, 3-oi-1
                fi, fj = ri+sx, rj+sy 
                test_arr[fi][fj] = prev_arr[i][j]
    return test_arr

def disappear_values():
    global arr 
    visited = [[False]*5 for _ in range(5)]
    result = [] # 삭제시킨 각 유물들의 path
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = True 
                que = deque()
                que.append((i, j))
                path = [(i, j)]
                while que:
                    x, y = que.popleft()
                    for dir in range(4):
                        nx, ny = x + dxs[dir], y + dys[dir]
                        if not in_range(nx, ny):continue 
                        if not visited[nx][ny] and arr[nx][ny] == arr[i][j]:
                            path.append((nx, ny))
                            que.append((nx, ny))
                            visited[nx][ny] = True
                if len(path) >= 3:
                    result += path
    return result
 
def fill_new_fragments(paths):
    global answer, arr
    paths.sort(key = lambda x : (x[1], -x[0]))
    for x, y in paths:
        answer += 1
        arr[x][y] = fragments.popleft()


def simulate():
    global arr
    candidates = []

    # 가장 1차 획득 가치가 높은 3*3 배열 찾기 
    for r_cnt in range(1, 4):
        for j in range(3):
            for i in range(3):
                test_arr = test_rotate_90(i, j, r_cnt)
                values = first_get_values(test_arr)
                candidates.append((values, r_cnt, j+1, i+1))
    candidates.sort(key = lambda x:(-x[0], x[1], x[2], x[3]))

    value, r_cnt, sy, sx = candidates[0]
    sy, sx = sy-1, sx-1

    # real로 r_cnt만큼 돌려주기
    r_arr = deep_copy(arr)
    for _ in range(r_cnt):
        prev_arr = deep_copy(r_arr)
        for i in range(sx, sx+3):
            for j in range(sy, sy+3):
                oi, oj = i-sx, j-sy 
                ri, rj = oj, 3-oi-1
                fi, fj = ri+sx, rj+sy 
                r_arr[fi][fj] = prev_arr[i][j]
    

    arr = deep_copy(r_arr)
    # print("회전한 뒤 arr")
    # for row in r_arr:
    #     print(*row)

    while first_get_values(arr) > 0:
        # print("values =", first_get_values(arr))
        paths = disappear_values()
        fill_new_fragments(paths)
    #     for row in arr:
    #         print(*row)
    # print()
    

for _ in range(k):
    answer = 0
    simulate()
    if answer == 0:
        break
    else:
        print(answer, end = " ")