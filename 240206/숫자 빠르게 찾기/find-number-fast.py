import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(target):
    global arr
    left,right = 0, n-1
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
    print(binary_search(target))