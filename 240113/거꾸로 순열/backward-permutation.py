import sys
input = sys.stdin.readline


n = int(input())
visited = [False]*(n+1)

def print_(sel):
    for ele in sel:
        print(ele, end=" ")
    print()

def choose(selected):
    if len(selected) == n:
        print_(selected)
        return 
    
    for i in range(n, 0, -1):
        if visited[i]:continue
        selected.append(i)
        visited[i] = True

        choose(selected)

        selected.pop()
        visited[i] = False
choose([])