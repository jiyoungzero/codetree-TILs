n,m = map(int ,input().split())
arr = list(map(int, input().split()))

def binary(target):
    start, end = 0, n-1
    result = -1
    while start <= end:
        mid = (start+end) // 2 
        if arr[mid] == target:
            return mid+1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

for _ in range(m):
    target = int(input())
    print(binary(target))