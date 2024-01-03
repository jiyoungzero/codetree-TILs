import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

# xor : ^
def backtracking(depth, selected):
    global answer

    if len(selected) == m:
        result = selected[0]
        for i in range(1, m):
            result ^= selected[i]
        answer = max(answer, result)
        return 
    if depth == n:
        return
    
    selected.append(arr[depth])
    backtracking(depth+1, selected)
    selected.pop()

    backtracking(depth+1, selected)
backtracking(0, [])

print(answer)