import sys
input = sys.stdin.readline

n = int(input()) # 장소의 개수
energy = list(map(int, input().split())) # 장소 간 이동시 드는 에너지
cost = list(map(int, input().split())) # 에너지1을 채우는데 드는 비용

m = len(energy)
dp = [0]*(m)
dp[-1] = energy[-1] 
for i in range(m-2, -1, -1):
    dp[i] = dp[i+1] + energy[i]
dp = dp + [0]

answer = 0
# 다음 장소의 cost가 현재 cost보다 작다면 충전
# 아니라면 충전안함
# 대신 첫 위치에서 cost가 다음 cost보다 크더라도 충전
for i in range(n-1):
    if cost[i] < cost[i+1]:
        nxt = i+1
        while nxt < len(cost) and cost[i] < cost[nxt]:
            nxt += 1
        nxt = min(len(cost)-1, nxt)
        answer += (dp[i]-dp[nxt])*cost[i]
    else:
        if i == 0:
            answer += (dp[i]-dp[i+1])*cost[i]
    
    # plus = (dp[i]-dp[i+1])
    # answer += (cost[i]*plus)
    # if plus >= dp[i+1]:
    #     break
print(answer)