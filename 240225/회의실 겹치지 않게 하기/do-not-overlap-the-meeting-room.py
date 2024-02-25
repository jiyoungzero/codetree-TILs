import sys
input = sys.stdin.readline 

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key = lambda x : x[0])
answer = 0

ss, ee = schedule[0][0], schedule[0][1]
for s, e in schedule[1:]:
    if ee > s:
        answer += 1
    ss, ee = s, e
print(answer)