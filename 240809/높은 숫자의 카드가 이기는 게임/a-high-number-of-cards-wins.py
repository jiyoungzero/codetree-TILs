import sys
input = sys.stdin.readline 

n = int(input())
b_arr = [int(input()) for _ in range(n)]
a_arr = []
b_set = set(b_arr)

for num in range(1, 2*n+1):
    if num not in b_set:
        a_arr.append(num)

b_arr.sort()
a_arr.sort()
b_idx = 0 
answer = 0
for i, a in enumerate(a_arr):
    if a > b_arr[b_idx]:
        b_idx = min(b_idx+1, n-1)
        answer += 1
print(answer)