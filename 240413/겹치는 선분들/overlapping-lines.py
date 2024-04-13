import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
answer = 0
start = 0

segments = []
for _ in range(n):
    m, d = map(str, input().split())
    if d == 'R':
        segments.append((start, start+int(m)))
        start += int(m)
    else:
        segments.append((start-int(m), start))
        start -= int(m)

points = []
for idx, segment in enumerate(segments):
    s, e = segment
    points.append((idx, s, 1))
    points.append((idx, e, -1))

points.sort(key = lambda x:(x[0], x[1]))

tmp = 1
for i, x, v in points:
    tmp += v
    if tmp >= k:
        answer += 1
print(answer)