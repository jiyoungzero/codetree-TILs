import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
lines = []
answer = int(1e9)
for _ in range(m):
    col, row = map(int, input().split())
    lines.append((row-1, col-1))
lines.sort()
# print(lines)
def is_same(sel):
    result1 = [i for i in range(n)]
    result2 = [i for i in range(n)]

    for _, col in lines:
        result1[col], result1[col+1] = result1[col+1], result1[col]
    for _, col in sel:
        result2[col], result2[col+1] = result2[col+1], result2[col]
    for a, b in zip(result1, result2):
        if a != b:
            return False
    return True

def backtracking(depth, sel):
    global answer
    if depth >= len(lines):
        if is_same(sel):
            answer = min(len(sel), answer)
        return 
    
    sel.append(lines[depth])
    backtracking(depth+1, sel)
    sel.pop()

    backtracking(depth+1, sel)

backtracking(0, [])
print(answer)