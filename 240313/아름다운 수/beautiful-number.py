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
    cur_num = num[0]
    cnt = 1
    if len(num) == 1 and cur_num != 1:
        return False
    for i in range(1, n):
        if num[i] == cur_num:
            cnt += 1
        else:
            if cnt%cur_num != 0:
                return False
            else:
                cnt = 1
                cur_num = num[i]
    if cnt % cur_num != 0:
        return False
    return True

backtracking([])
print(answer)