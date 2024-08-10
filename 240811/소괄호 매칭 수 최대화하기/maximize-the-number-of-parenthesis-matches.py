import sys
input = sys.stdin.readline 
from functools import cmp_to_key

def custom_compare(item1, item2):
    o_cnt1, c_cnt1 = item1
    o_cnt2, c_cnt2 = item2
    if o_cnt1 * c_cnt2 > o_cnt2 * c_cnt1:
        return -1
    elif  o_cnt1 * c_cnt2 < o_cnt2 * c_cnt1:
        return 1
    else:
        return 0

answer = 0
n = int(input())
arr = []
for _ in range(n):
    ele = input().rstrip()
    o_cnt, c_cnt = 0, 0
    for e in ele:
        if e == '(': o_cnt += 1
        else: 
            c_cnt += 1
            answer += o_cnt
    arr.append((o_cnt, c_cnt))


arr.sort(key = cmp_to_key(custom_compare))

o_sum = 0
for o_cnt, c_cnt in arr:
    answer += (o_sum * c_cnt)
    o_sum += o_cnt
print(answer)