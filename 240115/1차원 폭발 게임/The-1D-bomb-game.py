import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def get_end_bomb_idx(cur_idx, number):
    for end_idx in range(cur_idx+1, len(arr)):
        if arr[end_idx] != number:
            return end_idx-1
    return len(arr)-1


while True:
    bomb_flag= False
    for cur_idx, number in enumerate(arr):
        if number == 0: 
            continue

        end_idx = get_end_bomb_idx(cur_idx, number)
        if end_idx - cur_idx + 1 >= m:
            arr[cur_idx:end_idx+1] = [0]*(end_idx-cur_idx+1)
            bomb_flag = True

    arr = list(filter(lambda x:x>0, arr))
    if not bomb_flag:break

print(len(arr))
for ele in arr:
    print(ele)