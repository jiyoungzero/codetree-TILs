import sys
input = sys.stdin.readline 

n = int(input())
lst = input().rstrip()

# 가장 거리가 먼 두 지점(a, b)를 구하고 해당 거리의 반이 되는 곳에 위치 
max_dist = 0
a, b = 0, 0
for i in range(n):
    if lst[i] == '1':
        tmp_dist = 0
        tmp_b = 0
        for j in  range(i+1, n):
            if lst[j] == '1':
                tmp_dist = (j-i)
                tmp_b = j
                break
        if max_dist < (tmp_dist):
            max_dist = tmp_dist
            a, b = i, tmp_b

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
final_dist = max(max_dist//2, left_dist, right_dist)
if final_dist == max_dist//2:
    idx = (b-a)//2
    lst = lst[:idx]+'1'+lst[idx+1:]
elif final_dist == left_dist:
    lst = '1'+lst[1:]
else:
    lst = lst[:-1]+'1'

# print(lst)
# 가장 짧은 거리 구하기
min_dist = int(1e9)
for i in range(n):
    if lst[i] == '1':
        tmp_dist = int(1e9)
        for j in range(i+1, n):
            if lst[j] == '1':
                tmp_dist = j-i
                break
        min_dist = min(min_dist, tmp_dist)
print(min_dist)