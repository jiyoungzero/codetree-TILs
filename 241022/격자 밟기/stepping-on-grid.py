k = int(input())
cant_lst = []
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    cant_lst.append((x-1, y-1))
    
routes = []
answer = 0
dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = [[False]*5 for _ in range(5)]
for x, y in cant_lst:
    visited[x][y] = True

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5 

def same_route(route):
    if route in routes:
        return True 
    return False

def all_visited():
    for i in range(5):
        for j in range(5):
            if not visited[i][j]: return False 
    return True 


def backtracking(x, y, a_route):
    global answer, visited, routes

    if (x, y) == (4,4) and all_visited() and not same_route(a_route):
        answer += 1
        routes.append(a_route)
        return 
    if all_visited():
        return 

    for dir in range(4):
        nx, ny = x + dxs[dir], y + dys[dir]
        if not in_range(nx, ny) or visited[nx][ny]:continue 
        visited[nx][ny] = True
        backtracking(nx, ny, a_route+[(nx, ny)])
        visited[nx][ny] = False

visited[0][0] = True
backtracking(0,0,[(0,0)])
print(answer)