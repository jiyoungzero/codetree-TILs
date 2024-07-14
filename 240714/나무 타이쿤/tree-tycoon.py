import sys
input = sys.stdin.readline 
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmds = []
medicines = [[n-2, 0],[n-2, 1], [n-1, 0], [n-1, 1]]

for _ in range(m):
    d, p = map(int, input().split())
    cmds.append((d-1, p))

answer = 0
dxs, dys = [0, -1,-1,-1,0,1,1,1], [1,1,0,-1,-1,-1,0,1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_medicine(d, p):
    global medicines
    n_medicines = []
    for x, y in medicines:
        nx = (x + dxs[d]*p) % n
        ny = (y + dys[d]*p) % n
        n_medicines.append([nx, ny])
    medicines = n_medicines

def grow_trees():
    global arr
    for x, y in medicines:
        arr[x][y] += 1

    for x, y in medicines:
        for dir in [1, 3, 5, 7]:
            nx, ny = x + dxs[dir], y + dys[dir]
            if in_range(nx, ny) and arr[nx][ny] >= 1: arr[x][y] += 1
  

def cut_and_put_new():
    global medicines, arr
    new_medicines = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not ([i, j] in medicines):
                arr[i][j] -= 2
                new_medicines.append([i, j])
    medicines = new_medicines


def get_answer():
    global answer
    for row in arr:
        answer += sum(row)


for t in range(m):
    move_medicine(cmds[t][0], cmds[t][1]) # 방향, 이동 칸 수
    grow_trees()
    cut_and_put_new()

get_answer()
print(answer)