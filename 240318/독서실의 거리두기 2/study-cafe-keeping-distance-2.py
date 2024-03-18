import sys
input = sys.stdin.readline 

n = int(input())
lst = input().rstrip()

# 가장 거리가 먼 두 지점(a, b)를 구하고 해당 거리의 반이 되는 곳에 위치 
max_dist = 0
for i in range(n):
    if lst[i] == '1':
        tmp_dist = 0
        for j in  range(i+1, n):
            if lst[j] == '1':
                tmp_dist = (j-i)
                break
        if max_dist < (tmp_dist):
            max_dist = tmp_dist

# 양 끝에서 놓았을 때 
left_dist, right_dist = 0, 0
if lst[0] != '1':
    left_dist = 1
    for ele in lst[1:]:
        if ele == '1':
            break
        else:
            left_dist += 1
if lst[::-1][0] != '1':
    right_dist = 1
    for ele in lst[::-1][1:]:
        if ele == '1':
            break
        else:
            right_dist += 1

# print(max_dist, left_dist, right_dist)
print(max(max_dist//2, left_dist, right_dist))