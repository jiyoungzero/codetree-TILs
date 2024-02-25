import sys
input = sys.stdin.readline 

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key = lambda x : x[1])
answer = 0

last_e, max_cnt = -1, 0
for s, e in schedule:
    if s >= last_e:
        max_cnt += 1
        last_e = e

answer = n - max_cnt
print(answer)

# 7
# 1 2
# 1 3
# 1 4
# 4 5
# 2 3
# 6 7
# 8 10