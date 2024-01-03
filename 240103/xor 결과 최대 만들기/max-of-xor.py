import sys
input = sys.stdin.readline
# import functools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def find_max_xor(cur_idx, cnt, cur_val):
    global answer
    if cnt == m:
        answer = max(answer, cur_val)
        return 

    if cur_idx == n:
        return 

    # 선택하는 경우
    find_max_xor(cur_idx+1, cnt+1, cur_val^arr[cur_idx])

    # 선택 안하는 경우
    find_max_xor(cur_idx+1, cnt, cur_val)

find_max_xor(0,0,0)
print(answer)