import sys
input = sys.stdin.readline 


n = int(input())
arr = []
for _ in range(n):
    command = input().rstrip()
    tmp = []
    flag = False
    for ele in command:
        if ele == '/':
            tmp.append(ele)
            continue
        if not flag:
            tmp.append('\\')
            flag = True
        if flag:
            flag = False
    arr.append(tmp)

            
start = int(input()) 
x, y = start//n, start%n-1
cur_dir = 0
up_slash = {0:3, 3:0, 2:1, 1:2}
down_slash = {0:1, 1:0, 2:3, 3:2}
if arr[x][y] == '\\': # 0: 밑으로, 1 : 오른쪽으로, 2: 위쪽으로, 3 : 왼쪽으로 
    cur_dir = down_slash[x]
else:
    cur_dir = up_slash[x]

dxs, dys = [1,0,-1,0], [0, 1,0,-1]
answer = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while True:
    # print(x, y, cur_dir)
    if arr[x][y] == '\\': # down_slash
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if not in_range(nx, ny):
            break
        x, y = nx, ny
        # 방향 바꾸기
        nxt_dir = down_slash[cur_dir]
        cur_dir = nxt_dir
    else: # up_slash
        nx, ny = x + dxs[nxt_dir], y + dys[nxt_dir]
        if not in_range(nx, ny):
            break
        x, y = nx, ny
        # 한번 더 방향 바꾸기
        nxt_dir = up_slash[nxt_dir]
        cur_dir = nxt_dir
    answer += 1
print(answer)