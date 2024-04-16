import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
dots = list(map(int, input().split()))

def lower_bound(target): # dots에서 target보다 같거나 작은 최소 인덱스
    max_idx = n
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if dots[mid] < target:
            s = mid+1
        else:
            e = mid - 1
            max_idx = min(max_idx, mid)            

    return max_idx
    

def upper_bound(target): # dots에서 target보다 초과하는 최소 인덱스
    max_idx = n
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if dots[mid] > target:
            e = mid - 1
            max_idx = min(max_idx, mid)
        else:
            s = mid+1
    return max_idx

for _ in range(m):
    start, end = map(int, input().split())
    print(upper_bound(end)-lower_bound(start))