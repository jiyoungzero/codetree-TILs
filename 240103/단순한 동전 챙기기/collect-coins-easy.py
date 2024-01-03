import sys
input = sys.stdin.readline


n = int(input())
maze = [input().rstrip() for _ in range(n)]
s_x, s_y = 0, 0
m = len(maze[0])
answer = int(1e9)
dxs, dys = [0,0,1,-1], [1,-1,0,0]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            s_x, s_y = i, j
            break

def solution(coin_lst, path_len,  x, y):
    global answer 
    if len(coin_lst) == 3 and maze[x][y] == 'E':
        answer = min(answer, path, len)
        print("asss", answer)
        return
    
    if len(coin_lst) == 3 or maze[x][y] == 'E':
        return
    
    for k in range(4):
        nx, ny = x+dxs[k], y +dys[k]
        print(x, y)
        if nx < 0 or n <= nx or ny < 0 or m <= ny:
            continue
        if visited[nx][ny]:
            continue

        if maze[nx][ny] == '.':
            visited[nx][ny] = True
            solution(coin_lst, path_len+1, nx, ny)

        elif maze[nx][ny].isdigit():
            visited[nx][ny] = True
            if len(coin_lst) == 0:
                coin_lst.append(int(maze[nx][ny]))
                solution(coin_lst, path_len+1, nx, ny)
                coin_lst.pop()              
            elif int(maze[nx][ny]) > coin_lst[-1]:
                coin_lst.append(int(maze[nx][ny]))
                solution(coin_lst, path_len+1, nx, ny)
                coin_lst.pop()
            else:
                solution(coin_lst, path_len+1, nx, ny)
        
solution([], 0, s_x, s_y)
print(answer)