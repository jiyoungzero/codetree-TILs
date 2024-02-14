import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
parent = [0]*(n+1)

finding_node = -1
answer = 0
for i in range(1, n+1):
    if nums[i] == k:
        finding_node = i

parent_node = 0
for i in range(2, n+1):
    if nums[i-1]+1 < nums[i]:
        parent_node += 1