import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def lower_bound(target):
    start, end = 0, n-1
    min_idx = n
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] >= target:
            min_idx = min(min_idx, mid)
            end = mid  - 1
    return min_idx
        

def upper_bound(target):
    start, end = 0, n-1
    min_idx = n
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            end  = mid - 1
        else:
            start = mid + 1
    return  min_idx

for _ in range(m):
    target = int(input())
    print(upper_bound(target)-lower_bound(target))