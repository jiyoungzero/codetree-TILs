n = int(input())
arr = [input() for _ in range(n)]
answer = int(1e9)
start, end = (0,0), (0,0)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == 'E':
            end = (i, j)
        
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs, dys = [0,0,1,-1], [1,-1,0,0]
def backtracking(path, coins, now):
    global answer
    if len(coins) == 3 and now == end:
        answer = min(answer, len(path))
        return 
    x, y = now
    for dir in range(4):
        nx, ny = x + dxs[dir], y + dys[dir]
        if in_range(nx, ny):
            if arr[nx][ny] == '.':
                path_len += 1
                backtracking()         
    
backtracking(path_len, [], start)
print(answer)