n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 답안

count = dict()

answer = 0
for ele in arr:
    diff = k - ele
    if diff in count:
        answer += count[diff]

    if ele in count:
        count[ele] += 1
    else:
        count[ele] = 1
print(answer)