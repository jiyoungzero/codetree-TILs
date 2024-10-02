import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
lst = []

def backtracking(sel, cnt):
    if sum(sel) > n:return

    if sum(sel) == n:
        lst.append(sel)
        if len(lst) == k:
            res = ""
            # print(*sel)
            for ele in sel:
                res += str(ele)
                res += "+"
            print(res[:-1])
        return

    for i in range(1, 4):
        sel.append(i)
        backtracking(sel, cnt)
        sel.pop()

backtracking([], 0)
if len(lst) < k:
    print(-1)