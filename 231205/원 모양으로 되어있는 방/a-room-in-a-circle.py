import sys
input =sys.stdin.readline


answer = float('inf')
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))


for s in range(n):
    tmp = 0
    for i in range(n):
        nxt_idx = (s+i)%n
        tmp += (arr[nxt_idx]*i)
    answer = min(answer, tmp)

print(answer)