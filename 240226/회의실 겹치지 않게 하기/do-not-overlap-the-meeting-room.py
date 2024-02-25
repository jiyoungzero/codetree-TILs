import sys
input = sys.stdin.readline 

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key = lambda x : x[1])
answer = 0

ss, ee = schedule[0][0], schedule[0][1]

for i in range(1, n):
    s, e = schedule[i]
    if ee <= s:
        ss, ee = s, e
        continue
    else:
        answer += 1
        ss, ee = schedule[i-2][0], schedule[i-2][1]

print(answer)