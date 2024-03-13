import sys
input = sys.stdin.readline 

n = int(input())
answer = 0

def backtracking(cur_num):
    global answer
    if len(cur_num) == n:
        if success(cur_num):
            answer += 1
        return 
    for i in range(1, 5):
        cur_num.append(i)
        backtracking(cur_num)
        cur_num.pop()

def success(num):
    idx = 0
    while idx < n:
        if idx + num[idx] - 1 >= n:
            return False
        for j in range(idx, idx+num[idx]):
            if num[j] != num[idx]:
                return False
            idx = idx+num[idx]
    return True

backtracking([])
print(answer)