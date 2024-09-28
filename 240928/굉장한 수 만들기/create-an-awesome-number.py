import sys
input = sys.stdin.readline 

def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1) + num 

n = int(input())
nums = [factorial(num) for num in range(1, 751)]
boxes = [0]*(750)
boxes[0] = 1
for i in range(1, 750):
    boxes[i] = boxes[i-1] + nums[i]

answer = 0
# dp 
dp = [0]*(n+1)
cur = 0
dp[1] = 1
for i in range(2, n+1):
    if boxes[cur+1] > i:
        min_value = int(1e9)
        for j in range(cur+1):
            min_value = min(min_value, dp[i-boxes[j]] + 1)
        dp[i] = min_value

    # cur의 값이 i보다 같거나 클 때 
    else:
        cur += 1
        if boxes[cur] == i:
            dp[i] = 1
        else:
            min_value = int(1e9)
            for j in range(cur+1):
                min_value = min(min_value, dp[i-boxes[j]] + 1)
            dp[i] = min_value
# print(boxes[:6])
print(dp[n])