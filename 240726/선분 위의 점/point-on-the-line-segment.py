import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def upper_bound(target):
    # target보다 초과인 수가 처음나오는 수! min
    l, r = 0, n-1
    idx = n
    while l <= r:
        mid = (l+r)//2
        if arr[mid] > target:
            idx = min(idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return idx

def lower_bound(target):
    # target보다 이상인 수가 처음 나오는 곳! min
    l, r = 0, n-1
    idx = n
    while l <= r:
        mid = (l+r)//2
        if arr[mid] >= target:
            idx = min(mid, idx)
            r = mid -1
        else:
            l = mid + 1
    return idx

for _ in range(m):
    s, e = map(int, input().split())
    print(upper_bound(e)-lower_bound(s))