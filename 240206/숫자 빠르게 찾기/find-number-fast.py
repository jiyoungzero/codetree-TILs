import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
before = 0

def binary_search(target, before):
    global arr
    left,right = before, n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid+1
        if arr[mid] < target:
            left += 1
        else:
            right -= 1
    return -1


for _ in range(m):
    target = int(input())
    before = binary_search(target,before)
    print(before)
    before -= 1