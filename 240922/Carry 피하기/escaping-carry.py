import sys
input = sys.stdin.readline 


n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0

def is_possible(lst):
    int2str = [str(ele) for ele in lst]
    max_len = 0
    for ele in int2str:
        max_len = max(max_len, len(ele))
    
    for idx, ele in enumerate(int2str):
        if max_len > len(ele):
            int2str[idx] = '0'*abs(len(ele) - max_len) + ele 
    
    for i in range(max_len):
        sum_val = 0
        for ele in int2str:
            sum_val += int(ele[i])
        if sum_val > 9:
            return False
    return True 
            

def backtracking(sel, depth):
    global answer
    if depth >= n:
        if is_possible(sel):
            answer = max(answer, len(sel))
        return 
    
    sel.append(arr[depth])
    backtracking(sel, depth+1)
    sel.pop()

    backtracking(sel, depth+1)

backtracking([], 0)
print(answer)