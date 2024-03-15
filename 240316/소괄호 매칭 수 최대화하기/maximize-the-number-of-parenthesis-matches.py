import sys
input = sys.stdin.readline 
from functools import cmp_to_key

n = int(input())
lsts = [input().rstrip() for _ in range(n)]
answer = 0

open_lst = []
for lst in lsts:
    open_ = 0
    close_ = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            open_ += 1
        else:
            close_ += 1
            answer += open_
    open_lst.append((open_, close_))

def compare(a1, a2):
    open1, close1 = a1
    open2, close2 = a2
    if open1*close2 > open2*close1: # 현재 순서가 맞음
        return -1
    if open1*close2 < open2*close1:
        return 1
    return 0 # 우선순위가 동일한 경우



open_lst.sort(key = cmp_to_key(compare))
open_cnt = 0
for open_, close_ in open_lst:
    answer += (open_cnt*close_)
    open_cnt += open_
    


print(answer)