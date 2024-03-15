import sys
input = sys.stdin.readline 

n = int(input())
lsts = [input().rstrip() for _ in range(n)]
answer = 0

def count_answer(case_):
    global answer
    len_ = len(case_)
    for i in range(len_):
        if case_[i] == '(':
            for j in range(i+1, len_):
                if case_[j] == ")":
                    answer += 1

open_lst = []
for lst in lsts:
    open_ = 0
    close_ = 0
    first_open_idx = 0
    first_close_idx = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            open_ += 1
            if open_ == 1:
                first_open_idx = i
        else:
            close_ += 1
            if close_ == 1:
                first_close_idx = i
    open_lst.append((open_//max(1, close_), close_, first_open_idx, first_close_idx, lst))
open_lst.sort(key = lambda x: ( -x[0], x[2], x[1], -x[3]))
case_ = ""
for ele in open_lst:
    case_ += ele[4]

# print(case_)
count_answer(case_)
print(answer)