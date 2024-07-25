import sys
input = sys.stdin.readline 



n, m = map(int, input().split())
arr = list(map(int, input().split()))

def upper_bound(target):
    s, e = 0, n-1
    idx = n
    while s <= e:
        mid = (s+e)//2
        if arr[mid] > target:
            idx = min(idx, mid)
            e = mid -1
        else:
            s = mid + 1
    return idx


def lower_bound(target):
    s, e = 0, n-1
    idx = n
    while s <= e:
        mid = (s+e)//2
        if arr[mid] >= target:
            idx = min(idx, mid)
            e = mid - 1
        else:
            s = mid + 1
    return idx

for _ in range(m):
    target = int(input())
    print(upper_bound(target)-lower_bound(target))