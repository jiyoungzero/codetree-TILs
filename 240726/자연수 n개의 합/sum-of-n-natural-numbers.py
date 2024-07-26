import sys
input = sys.stdin.readline 

s = int(input())
l, r = 1, 10**18
max_idx = -1

while l <= r:
    mid = (l+r)//2
    if mid*(mid+1)//2 <= s:
        max_idx = max(max_idx, mid)
        l = mid + 1
    else:
        r = mid - 1

print(max_idx)