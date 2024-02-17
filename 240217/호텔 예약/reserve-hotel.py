import sys
input = sys.stdin.readline 

n = int(input())
points = []
answer = 0

for i in range(n):
    s, e = map(int, input().split())
    points.append((s, 1))
    points.append((e, -1))

points.sort()
tmp = 0
for x, v in points:
    tmp += v
    answer = max(answer, tmp)
print(answer)