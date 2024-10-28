r, c = map(int, input().split())
arr = [input() for _ in range(r)]
dxs, dys = [1, 0], [0, 1] # 아래, 오른쪽 
answer = 0
visited = [[False]*c for _ in range(r)]

def backtracking(cur):
    global answer
    # print(cur)
    if cur == (r-1, c-1):
        answer += 1
        return 
    
    x, y = cur
    if x == r-1 or y == c-1:return

    for nx in range(x+1, r):
        for ny in range(y+1, c):
            if not visited[nx][ny]  and arr[x][y] != arr[nx][ny]:
                visited[nx][ny] = True
                backtracking((nx, ny))
                visited[nx][ny] = False

visited[0][0] = True
backtracking((0, 0))
print(answer)