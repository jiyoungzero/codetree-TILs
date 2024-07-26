import sys
input = sys.stdin.readline 

n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def upper_bound(target):
    # target이 해당 숫자보다 초과인 min_idx
    l, r = 0, n-1
    min_idx = n
    while l <= r:
        mid = (l+r)//2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_idx

def lower_bound(target):
    l, r = 0, n-1
    min_idx = n
    while l <= r:
        mid = (l+r)//2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_idx


for _ in range(q):
    a, b = map(int, input().split())
    print(upper_bound(b) - lower_bound(a))