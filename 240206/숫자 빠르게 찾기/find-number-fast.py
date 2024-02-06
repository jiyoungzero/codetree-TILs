import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
before = 0

def binary_search(target):
    global arr
    left,right = 0,n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left += 1
        else:
            right -= 1
    return -1


for _ in range(m):
    target = int(input())
    index = binary_search(target)
    print(index+1 if index > -1 else -1)