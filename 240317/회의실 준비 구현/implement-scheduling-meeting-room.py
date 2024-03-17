import sys
input = sys.stdin.readline 

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
answer = 1

arr.sort(key = lambda x:x[1])
prev_s, prev_e = arr[0]

for s, e in arr[1:]:
    if prev_e <= s:
        answer += 1
        prev_e = e 
print(answer)