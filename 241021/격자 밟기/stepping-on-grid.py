k = int(input())
cant_lst = set(tuple(map(int, input().split())) for _ in range(k))
routes = []
answer = 0
dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = [[False]*5 for _ in range(5)]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5 

def same_route(a, b):
    if (a, b) in routes:
        return True 
    return False

def all_visited():
    for i in range(5):
        for j in range(5):
            if not visited[i][j]: return False 
    return True 

def backtracking(ax, ay, bx, by, a_route, b_route):
    global answer, visited, routes
    print(a_route, b_route)
    if (ax, ay) == (bx, by) and all_visited() and not same_route(a_route, b_route):
        routes.append((a_route, b_route))
        answer += 1
        return 

    if all_visited():
        return 
    
    a_dir = -1
    for dir in range(4):
        n_ax, n_ay = ax + dxs[dir], ay + dys[dir]
        if not in_range(n_ax, n_ay) or visited[n_ax][n_ay] or (n_ax, n_ay) in cant_lst:
            continue 
        else:
            a_dir = dir
            break

    b_dir = -1
    for dir in range(4):
        n_bx, n_by = bx + dxs[dir], by + dys[dir]
        if in_range(n_bx, n_by) and not visited[n_bx][n_by] and (n_bx, n_by) not in cant_lst:
            b_dir = dir
            print((bx+dxs[dir], by+dys[dir]), in_range(bx+dxs[dir], by+dys[dir]))
            break

    a_route.append((ax+dxs[a_dir], ay +dys[a_dir]))
    b_route.append((bx+dxs[b_dir], by+dys[b_dir]))
    
    visited[ax+dxs[a_dir]][ay +dys[a_dir]] = True
    print((bx+dxs[b_dir], by+dys[b_dir]))
    visited[bx+dxs[b_dir]][by +dys[b_dir]] = True
    backtracking(ax+dxs[a_dir], ay +dys[a_dir], bx+dxs[b_dir], by+dys[b_dir], a_route, b_route)
    a_route.pop()
    b_route.pop()
    visited[ax+dxs[a_dir]][ay +dys[a_dir]] = False
    visited[bx+dxs[b_dir]][by +dys[b_dir]] = False

backtracking(0,0,4,4,[],[])
print(answer)