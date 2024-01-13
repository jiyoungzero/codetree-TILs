import sys
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
answer = []

def print_answer(sel):
    for ele in sel:
        print(ele, end=" ")
    print()

def choose(selected):
    if len(selected) == n:
        print_answer(selected)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True

        choose(selected)
        
        visited[i] = False
        selected.pop()

choose([])