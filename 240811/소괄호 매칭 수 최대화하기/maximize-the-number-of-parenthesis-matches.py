import sys
input = sys.stdin.readline 
from functools import cmp_to_key

def custom_compare(item1, item2):
    o_cnt1, c_cnt1, _ = item1
    o_cnt2, c_cnt2, _ = item2
    if o_cnt1 * c_cnt2 > o_cnt2 * c_cnt1:
        return -1
    elif  o_cnt1 * c_cnt2 < o_cnt2 * c_cnt1:
        return 1
    else:
        return 0


n = int(input())
arr = []
for _ in range(n):
    ele = input().rstrip()
    o_cnt, c_cnt = 0, 0
    for e in ele:
        if e == '(': o_cnt += 1
        else: c_cnt += 1
    arr.append((o_cnt, c_cnt, ele))


arr.sort(key = cmp_to_key(custom_compare))
result = ''
for ele in arr:
    result += ele[2]

n = len(result)

prefix = [0]*n

prefix[0] = 1 if result[0] == ")" else 0
for i in range(1, n):
    if result[i] == ")":
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] = prefix[i-1]

answer = 0
for i in range(n):
    if result[i] == "(":
        answer += (prefix[-1]-prefix[i])
print(answer)