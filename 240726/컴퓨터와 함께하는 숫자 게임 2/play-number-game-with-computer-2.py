import sys
input = sys.stdin.readline 

m = int(input())
arr = list(range(1, m+1))
a, b = map(int, input().split())


def binary_search(target):
    l, r = 0, m-1
    result = 0
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return result+1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        result += 1
    
answer = []
for target in range(a, b+1):
    answer.append(binary_search(target))
print(min(answer), max(answer))