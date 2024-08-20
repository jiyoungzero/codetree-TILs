import sys
input = sys.stdin.readline 

n = int(input())
dists = [0]*2 + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# i번째 장소로 출발할 때, 가장 cost가 적은 곳으로 전처리
# min_cost = [0]*(n+1)
# min_cost[1] = costs[1]
# for i in range(2, n+1):
#     min_cost[i] = min(min_cost[i-1], costs[i])
min_cost = [0] * (n + 1)
min_cost[2] = costs[1]
for i in range(3, n+1):
    min_cost[i] = min(min_cost[i-1], costs[i-1])
# print(min_cost)

# [0, 0, 2, 3, 1]
# [0, 0, 5, 2, 2]
answer = 0
for i in range(1, n+1):
    answer += min_cost[i] * dists[i]
print(answer)