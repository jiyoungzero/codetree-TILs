import sys
input = sys.stdin.readline

n = int(input())
answer = 0

def backtracking(num, depth):
    global answer
    if depth == n:
        answer += 1
        return 
    
    for i in range(1, 4):
        if beautiful(num):
            num.append(i)
            backtracking(num, depth+1)
            num.pop()

        backtracking(num, depth)

def beautiful(num):
    for i in range(len(num)):
        target = num[i]
        cnt = 0
        for j in range(i, len(num)):
            if num[j] == target:
                cnt += 1
            else:break
        if cnt % target != 1:
            return False
    return True

print(backtracking([], 0))