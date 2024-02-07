from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
targets = list(map(int, input().split()))
targets.sort()
for _ in range(m):
    a, b = map(int, input().split())
    left_idx = bisect_left(targets, a)
    right_idx = bisect_right(targets, b)
    print(right_idx-left_idx)