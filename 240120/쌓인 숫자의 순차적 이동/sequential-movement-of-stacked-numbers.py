import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dxs, dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0 , 1, -1, 1, -1, 0, 1]
stack_arr = [[[]*n for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        stack_arr[i][j].append(arr[i][j])

def in_range(x, y):
    return 0 <= x < n and 0<= y < n 

def find_ij_idx(num):
    for i in range(n):
        for j in range(n):
            for idx, ele  in enumerate(stack_arr[i][j]):
                if ele == num:
                    return (i, j, idx)

def get_max_ij(x, y):
    tmp_max = 0
    result = (0, 0)
    for k in range(8):
        nx, ny = x+dxs[k], y+dys[k]
        if not in_range(nx, ny):continue
        for ele in stack_arr[nx][ny]:
            if ele > tmp_max:
                result = (nx, ny)
                tmp_max = ele
    return result

        


for command in commands:
    # 해당 숫자 위치 찾기
    i, j, move_idx = find_ij_idx(command)
    

    # 8방향에서 최댓값, index찾기 
    mi,mj = get_max_ij(i, j)

    # stack_arr 위치에 append
    stack_arr[mi][mj] += stack_arr[i][j][move_idx:]
    del stack_arr[i][j][move_idx:]

    
for i in range(n):
    for j in range(n):
        if len(stack_arr[i][j]) == 0:
            print("None")
        else:
            for ele in stack_arr[i][j][::-1]:
                print(ele, end=' ')
            print()