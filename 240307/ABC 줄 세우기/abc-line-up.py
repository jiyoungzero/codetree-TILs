import sys
input = sys.stdin.readline 

n = int(input())
answer = 0
arr = list(map(str, input().split()))
correct = sorted(arr)

def right_idx(lst, target):
    right_lst = sorted(lst)
    right_lst_idx = right_lst.index(target)
    return right_lst_idx == lst.index(target)

def get_right_idx(lst, target):
    right_lst = sorted(lst)
    return right_lst.index(target)

# while True:
#     if arr == correct:
#         break
for ele in sorted(arr)[::-1]:
    if right_idx(arr, ele):continue
    else:
        while not right_idx(arr, ele):
            right_idx_ = get_right_idx(arr, ele)
            prev_idx = arr.index(ele)
            if prev_idx < right_idx_:
                arr[prev_idx], arr[prev_idx+1] = arr[prev_idx+1], arr[prev_idx]
            else:
                arr[prev_idx-1], arr[prev_idx] = arr[prev_idx], arr[prev_idx-1]
            answer += 1
 
print(answer)