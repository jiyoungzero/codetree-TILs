n = int(input())
arr = [input() for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def right_one(ele): # 굉장히 올바른 문자열인지 
    flag = False # ')'가 나왔는지
    if ele.count(')') != ele.count('('):
        return False 
        
    for i in range(len(ele)):
        if i != len(ele)-1 and ele[i] == ')':
            flag = True 
        if ele[i] == '(' and flag:
            return False 
    return True 

dxs, dys = [0,0,1,-1], [1,-1,0,0]


visited = [[False]*n for _ in range(n)]
answer = 0

def all_visited():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:return False 
    return True 

def backtracking(x, y, cur, depth):
    global visited, answer

    if len(cur) and right_one(cur):
        answer = max(answer, len(cur))

    if all_visited():
        return 
    
    for dir in range(4):
        nx, ny = x + dxs[dir], y + dys[dir]
        if not in_range(nx, ny): continue 
        if visited[nx][ny] != False or (visited[nx][ny] != False and visited[nx][ny] < depth): continue

        visited[nx][ny] = depth 
        backtracking(x+dxs[dir], y+dys[dir], cur+arr[nx][ny], depth+1)
        visited[nx][ny] = False 

visited[0][0] = 1
backtracking(0, 0, arr[0][0], 2)
print(answer)