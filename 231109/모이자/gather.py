import sys

n = int(input())
house = list(map(int, input().split()))
answer = sys.maxsize

for i in range(n): # 모이는 집
    tmp = 0
    for j in range(n):
        tmp += house[j]*(abs(j-i))
    answer = min(answer, tmp)

print(answer)