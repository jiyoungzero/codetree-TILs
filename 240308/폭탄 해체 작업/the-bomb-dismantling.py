import sys
input = sys.stdin.readline 

n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(key = lambda x:(x[1], -x[0]))
bombs_flag = [False]*n
answer = 0

time = 0

for i, bomb in enumerate(bombs):
    grade, limit_time = bomb
    if limit_time > time:
        bombs_flag[i] = True
        answer += grade
    else:
        bombs_flag[i] = True
    time += 1    
print(answer)