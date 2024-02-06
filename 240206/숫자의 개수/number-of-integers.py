import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
from bisect import bisect_left,bisect_right

for _ in range(m):
    target = int(input())
    left_idx, right_idx = bisect_left(arr, target), bisect_right(arr, target)
    print(right_idx-left_idx)