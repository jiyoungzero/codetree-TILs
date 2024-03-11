import sys
input = sys.stdin.readline 
from itertools import combinations_with_replacement

n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] 
result = 0
answer = 0
def backtracking(row, sel, depth):
    global result
    if len(sel) == m:
        weight = 0
        for j in sel:
            weight += arr[row][j]
        if weight <= c:
            for j in sel:
                result += (arr[row][j])**2
        else:
            # c가 넘지 않는 선에서 고르기
            sel_arr_ele = [arr[row][j] for j in sel]
            sel_arr_ele.sort(reverse = True)
            tmp = 0
            now_idx = 0
            while tmp <= c:
                tmp += sel_arr_ele[now_idx]**2
                now_idx += 1
            tmp -= sel_arr_ele[now_idx-1]**2
            result += tmp
        return 

    if depth >= n:
        return
    
    sel.append(depth)
    visited
    backtracking(row, sel, depth+1)
    sel.pop()

    backtracking(row, sel, depth+1)
                
            

# 행 고르기
row_lst = list(combinations_with_replacement([i for i in range(n)], 2))
for a, b, in row_lst:
    result = 0
    visited = [False]*n # 겹치지 않기 위해서
    backtracking(a)
    backtracking(b)
    answer = max(answer, result)

print(answer)