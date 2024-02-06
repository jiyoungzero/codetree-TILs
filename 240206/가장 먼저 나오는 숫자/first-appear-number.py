from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
arr = list(map(int, input().split()))
targets = list(map(int, input().split()))
answer = []
for target in targets:
    l_idx = bisect_left(arr, target)
    r_idx = bisect_right(arr, target)
    if l_idx == r_idx:
        answer.append(-1)
    else:
        answer.append(l_idx+1)

for ele in answer:
    print(ele)