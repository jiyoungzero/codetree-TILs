import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
avg = sum(arr)//n

for ele in arr:
    if avg > ele:
        answer += (avg-ele)
print(answer)