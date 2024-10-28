r, c = map(int, input().split())
arr = [input() for _ in range(r)]
dxs, dys = [1, 0], [0, 1] # 아래, 오른쪽 
answer = 0

def backtracking(cur):
    global answer
    # print(cur)
    if cur == (r-1, c-1):
        answer += 1
        return 

    
    x, y = cur
    for i in range(1, r):
        for j in range(1, c):
            nx = x + dxs[0]*i
            ny = y + dys[1]*j
            if nx < r and ny < c and arr[x][y] != arr[nx][ny]:
                backtracking((x + dxs[0]*i,  y+ dys[1]*j))


backtracking((0, 0))
print(answer)