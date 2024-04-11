import sys
input = sys.stdin.readline 

n =int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
answer = int(1e9)

def get_cost(lst):
    result = 0
    if graph[0][lst[0]] == 0 or graph[lst[-1]][0] == 0:
        return False
    result += graph[0][lst[0]] 
    result += graph[lst[-1]][0]

    for i in range(len(lst)-1):
        if graph[lst[i]][lst[i+1]] == 0:
            return False
        else:
            result += graph[lst[i]][lst[i+1]]
    return result
    


def backtracking(depth, cur):
    global answer
    if len(cur) == n-1:
        # 비용 구하기
        if get_cost(cur) != False:
            answer = min(answer, get_cost(cur))
        return

    for i in range(1,n):
        if visited[i]:continue

        cur.append(i)
        visited[i] = True
        backtracking(depth+1, cur)
        

        cur.pop()
        visited[i] = False

        

backtracking(0, [])
print(answer)