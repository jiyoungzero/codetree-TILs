import sys
input = sys.stdin.readline 

n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(key = lambda x:(x[1], -x[0]))
bombs_flag = [False]*n
answer = 0

# print(bombs)
time = 0
for i, bomb in enumerate(bombs):
    grade, limit_time = bomb
    if i == n-1 and limit_time > time:
        answer += grade
        break
    
    if limit_time > time and bombs[i+1][0] < grade:
        answer += grade
        time += 1
    else:
        continue
      
        
print(answer)