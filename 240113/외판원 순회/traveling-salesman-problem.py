import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
answer = int(1e9)

def choose(selected):
    global answer
    if len(selected) == n:
        selected = selected + [0]
        if arr[selected[-2]][selected[-1]] == 0:
            return
        else:
            answer = min(get_min_route(selected), answer)
        return 
    for i in range(1, n):
        if visited[i] or arr[selected[-1]][i] == 0: continue
        selected.append(i)
        visited[i] = True

        choose(selected)

        selected.pop()
        visited[i] = False

def get_min_route(sel):
    i = 1
    from_, to_ = sel[0], sel[i]
    result = 0
    while to_ != sel[-1]:
        result += arr[from_][to_]
        from_ = to_
        i += 1
        to_ = sel[i]
    result += arr[from_][to_]
        
    return result
        


choose([0])
print(answer)