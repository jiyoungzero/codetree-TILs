import sys
input = sys.stdin.readline 

def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1) + num 

n = int(input())
nums = [factorial(num) for num in range(1, 701)]
boxes = [0]*(700)
boxes[0] = 1
for i in range(1, 700):
    boxes[i] = boxes[i-1] + nums[i]

answer = 0
# greedy 
for box in boxes[::-1]:
    if box <= n:
        answer += (n//box)
        n %= box 
print(answer)