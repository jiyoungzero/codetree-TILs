import sys
input = sys.stdin.readline 

n = int(input())
checked = [0]*(2*n)
points = []

for _ in range(n):
    s, e = map(int, input().split())
    points.append((s, 1))
    points.append((e, -1))
points.sort()

answer = 0
tmp = 0
for x, v in points:
    tmp += v
    answer = max(answer, tmp)

print(answer)