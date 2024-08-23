import sys

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

max_idx = [-sys.maxsize]*7
min_idx = [sys.maxsize]*7

# min_idx[0] = 0
# max_idx[0] = 0
sum_div = 0
for i in range(1, n+1):
    sum_div += arr[i]
    sum_div %= 7

    max_idx[sum_div] = max(max_idx[sum_div], i)
    min_idx[sum_div] = min(min_idx[sum_div], i)

answer = 0
for i in range(7):
    answer = max(answer, max_idx[i] - min_idx[i])
print(answer)