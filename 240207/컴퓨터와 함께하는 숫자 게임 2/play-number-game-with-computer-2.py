import sys
input = sys.stdin.readline 


m = int(input())
a, b = map(int, input().split())
min_answer = int(1e9)
max_answer = -1

def binary_search(target):
    global min_answer, max_answer

    left, right = 1, m
    time = 1
    while left <= right:
        mid = (left+right)//2
        if mid == target:
            min_answer = min(time, min_answer)
            max_answer = max(time, max_answer)
            return 
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
        time += 1

for target in range(a, b+1):
    binary_search(target)

print(min_answer, max_answer)