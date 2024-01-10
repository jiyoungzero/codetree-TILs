import sys
input =sys.stdin.readline

n = int(input())
energy =list(map(int, input().split()))+ [0]
cost = list(map(int, input().split()))
min_cost = [0]*n
min_cost[0] = cost[0]
answer = 0


for i in range(1, n):
    min_cost[i] = min(min_cost[i-1], cost[i])


for c, e in zip(min_cost, energy):
    answer += c*e

print(answer)