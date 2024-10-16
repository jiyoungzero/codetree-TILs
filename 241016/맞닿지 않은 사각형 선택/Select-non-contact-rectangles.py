n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

up_down, down_up = [0]*(n+1), [0]*(n+1)


for j in range(n):
    if j%2 == 0:
        up_down[j+1] = up_down[j] + arr[0][j]
        down_up[j+1] = down_up[j] + arr[1][j]
    else:
        up_down[j+1] = up_down[j] + arr[1][j]
        down_up[j+1] = down_up[j] + arr[0][j]
# print(up_down)[0, 1, 5, 6, 11, 21, 23, 27]
# print(down_up)[0, 2, 5, 8, 13, 19, 21, 29]

dp = [0]*(n+1)
dp[1] = max(up_down[1], down_up[1])
prev_i = 0 if up_down[1] > down_up[1] else 1
# up_down : 홀수인덱스일 때 -> 0, 짝수 인덱스일 때 -> 1
# down_up : 홀수인덱스 일 때 -> 1, 짝수 인덱스 -> 0

# 현재값 + (현재인덱스와 반대인 prefix), 현재 값 + (현재 인덱스와 같은 prefix + 그 전의 누적합)
for j in range(2, n+1):
    cur_num = max(arr[0][j-1], arr[1][j-1])
    cur_i = 0 if arr[0][j-1] else 1

    if cur_i == 0:
        same_dir = down_up
        opp_dir = up_down
    else:
        same_dir = up_down
        opp_dir = down_up
    dp[j] = max(opp_dir[j], same_dir[j-1], same_dir[j], cur_num + opp_dir[j-2])
    # print(dp)
print(dp[-1])