n = int(input())
arr = [input() for _ in range(n)]
answer = int(1e9)
start, end = (0,0), (0,0)
coins = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == 'E':
            end = (i, j)
        elif arr[i][j] != '.':
            coins.append((int(arr[i][j]), i, j))

coins.sort()

def get_dist(a, b):
    ax,ay = a 
    bx, by = b 
    return abs(ax-bx) + abs(ay-by)

def calc(selected):
    sum_dist =get_dist(start, selected[0])
    for i in range(2):
        sum_dist += get_dist(selected[i], selected[i+1])
    sum_dist += get_dist(selected[-1], end)
    return sum_dist


def backtracking(cur_idx, cnt, selected):
    global answer
    if cnt == 3:
        answer = min(answer, calc(selected))
    if cur_idx == len(coins):
        return 

    selected.append(coins[cur_idx][1:])
    backtracking(cur_idx+1, cnt+1, selected)
    selected.pop()

    backtracking(cur_idx+1, cnt, selected)

backtracking(0, 0, [])
print(answer if answer < int(1e9) else -1)