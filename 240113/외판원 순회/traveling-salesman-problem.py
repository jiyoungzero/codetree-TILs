import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
answer = int(1e9)

def choose(selected):
    global answer
    if len(selected) == n:
        answer = min(get_min_route(selected+[0]), answer)
        return 
    for i in range(1, n):
        if visited[i]:continue
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
    result += arr[sel[-2]][sel[-1]]
        
    return result
        


choose([0])
print(answer)