import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
visited = [False]*n
result = []

def choose(selected):
    global answer
    if len(selected) == n:
        tmp = 0
        for i, j in zip(selected, [i for i in range(n)]):
            tmp += arr[i][j]

        answer = max(answer, tmp)
        return 

    for i in range(n):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        choose(selected)
        
        visited[i] = False
        selected.pop()



choose([])
print(answer)