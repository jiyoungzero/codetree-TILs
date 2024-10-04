import sys
input = sys.stdin.readline 

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

def backtracking(idx, sum_value):
    global answer 
    # print(answer, sum_value)
    if idx >= n:
        # print(answer, sum_value)
        answer = max(answer, sum_value)
        return 

    t, p = arr[idx]
    if idx + t <= n:
        # 선택함 
        backtracking(idx+t, sum_value+p)
        # 안함
        backtracking(idx+1, sum_value)

backtracking(0, 0)
print(answer)