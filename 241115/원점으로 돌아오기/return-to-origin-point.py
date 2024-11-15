n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

def all_visited(sel):
    return n == len(set(sel))

def backtracking(sel, visited):
    global answer
    # 모든 경우의 수 -> x축, y축에 평행한 가? -> answer += 1
    if all_visited(sel):
        print(sel)
        answer += 1
        return 
    if all(visited):
        return

    print(sel)
    if sel:
        prev_x, prev_y = sel[-1]
        for i in range(n):
            cur_x, cur_y = dots[i]
            if prev_x == cur_x or prev_y == cur_y and not visited[i]:
                visited[i] = True
                backtracking(sel+[dots[i]], visited)
                visited = False
                backtracking(sel)
    else:
        for i in range(n):
            visited[i] = True
            backtracking(sel+[dots[i]], visited)
            visited[i] = False
            backtracking(sel, visited)
        
backtracking([], [False]*n)
print(answer)

    
    