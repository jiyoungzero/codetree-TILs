from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
targets = list(map(int, input().split()))
ranges = []
for _ in range(m):
    a, b = map(int, input().split())
    ranges.append()
answer = [0]*m 

for target in targets:
    for start, end in ranges:
        idx = bi