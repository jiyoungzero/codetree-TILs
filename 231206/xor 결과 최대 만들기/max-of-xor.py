import sys
input = sys.stdin.readline

# xor 연산 : ^
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


def do_xor(lst):
    result = 1
    if len(lst) > 1:
        for ele in lst[1:]:
            result ^= ele
    return result

def backtracking(selected, depth):
    global answer
    if depth == m:
        answer = max(answer, do_xor(selected))
        return
    for i in range(depth, n):
        selected.append(arr[i])
        backtracking(selected, depth+1)
        selected.pop()

        backtracking(selected, depth+1)

backtracking([], 0)
print(answer)