import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

plus, zero, minus = 0, 0, 0
for ele in arr:
    if ele == 0:
        zero += 1
    elif ele > 0:
        plus += 1
    else:
        minus += 1
# 양수 배열
if plus >= 3 and minus >= 3:
    answer = max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[2], arr[0]*arr[1]*arr[-1])
    
elif plus == 2:
    if minus >= 2:
        answer = arr[0]*arr[1]*arr[-1]
    else:
        if zero > 0:
            answer = 0
        else:
            answer = arr[-1]*arr[-2]*arr[-3]
elif plus == 1:
    if minus >=2 :
        answer = arr[0]*arr[1]*arr[-1]
    else:
        if zero > 0:
            answer = 0
        else:answer = arr[-1]*arr[-2]*arr[-3]

else:
    if zero > 0:
        answer = 0
    else:
        answer = answer = arr[-1]*arr[-2]*arr[-3]
print(answer)



# 양수 + 음수 배열 [-1, -2, -3, -4, 0, 1, 2]


# 음수 배열