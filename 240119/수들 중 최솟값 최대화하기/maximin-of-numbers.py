import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
visited = [False]*n
cases = []

def get_min_value(tmp):
    result = int(1e9)
    for idx, value in enumerate(tmp):
        result = min(result, arr[idx][value])
    return result

# 행 인덱스의 순열
def backtracking(depth):
    global cases, visited, answer
    if depth == n:
        answer = max(answer, get_min_value(cases))
        return 

    for i in range(n):
        if visited[i]:continue
        cases.append(i)
        visited[i] = True
        backtracking(depth+1)

        cases.pop()
        visited[i] = False

backtracking(0)
print(answer)