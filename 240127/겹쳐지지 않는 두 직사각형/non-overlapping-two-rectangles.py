import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = -int(1e9)
cases = []
board = [[0]*m for _ in range(n)]

for si in range(n):
    for sj in range(m):
        for ei in range(si, n):
            for ej in range(sj, m):
                cases.append((si, sj, ei, ej))

def get_sum(idx):
    global board
    result = 0
    si, sj, ei, ej = cases[idx]
    for x in range(si, ei+1):
        for y in range(sj, ej+1):
            result += arr[x][y]
            board[x][y] += 1
    return result

def duplicate():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False


for i in range(len(cases)):
    for j in range(i+1, len(cases)):
            board = [[0]*m for _ in range(n)]
            first = get_sum(i)
            second = get_sum(j)
            if duplicate():
                continue
            else:
                answer = max(answer, first+second)

print(answer)