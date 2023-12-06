import sys
input = sys.stdin.readline

# xor 연산 : ^
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
visited = [False]*(n+1)


def do_xor():
    result = 0
    for i in range(n):
        if visited[i]:
            result ^= arr[i]
    return result

def backtracking(depth, cnt):
    global answer
    if cnt == m:
        answer = max(answer, do_xor())
        return
    
    if depth == n:
        return 
    

    visited[depth] = True
    backtracking(depth+1, cnt+1)
    visited[depth] = False

    backtracking(depth + 1,cnt)
        



backtracking(0,0)
print(answer)