import sys
input = sys.stdin.readline

def success(lst):
    lst.sort()
    for i in range(2):
        if lst[i] + 1 != lst[i+1]:
            return False
    return True
arr = list(map(int, input().split()))
answer = 0

while success(arr) == False:
    # print(arr)
    f_gap, s_gap = abs(arr[0]-arr[1]), abs(arr[1]-arr[2])
    if f_gap < s_gap:
        if s_gap % 2 == 0:
            jump = s_gap//2
        else:
            jump = s_gap//2 +1
        arr[0] = arr[1] + jump
    else:
        if f_gap % 2 == 0:
            jump = f_gap//2
        else:
            jump = f_gap//2 +1
        arr[2] = arr[0] + jump
    arr.sort()
    answer += 1

    

print(answer)