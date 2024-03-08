import sys
input = sys.stdin.readline 
from bisect import bisect_left, bisect_right

n = int(input())
answer = 0

b_arr = [int(input()) for _ in range(n)]
a_arr = []
for i in range(1, 2*n+1):
    if i not in b_arr:
        a_arr.append(i)
a_arr.sort()
b_arr.sort()


b_idx = 0
for a_idx in range(n):
    if b_idx < n and a_arr[a_idx] > b_arr[b_idx]:
        b_idx += 1
        answer += 1

print(answer)