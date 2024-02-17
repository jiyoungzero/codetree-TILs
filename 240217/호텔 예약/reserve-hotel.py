import sys
input = sys.stdin.readline 

n = int(input())
points = []
answer = 1

for i in range(n):
    s, e = map(int, input().split())
    points.append((s, e))

points.sort()
s, e = points[0]

for point in points[1:]:
    ns, ne = point
    if ns >= e:
        s, e = ns, ne
    else:
        answer += 1
        s, e = ns, ne
print(answer)