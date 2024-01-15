import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
bomb_flag = True

def remove(start, cnt):
    global arr
    next_arr = []
    for i in range(start, start+cnt):
        arr[i] = 0
    for ele in arr:
        if ele:
            next_arr.append(ele)
    return next_arr

def consecutive(arr):
    flag = False
    start, cnt = 0, 1
    N = len(arr)
    for i in range(N-1):
        if arr[i] != arr[i+1] and cnt >= m:
            start = i-cnt+1
            flag = True
            break
        if arr[i] == arr[i+1]:
            cnt += 1
        if i+1 == N-1 and cnt >= m:
            start = i
            flag = True
            break
    
        
    return (flag, start, cnt)


while 1:
    N = len(arr)
    bomb_flag, start, cnt = consecutive(arr)
    if not bomb_flag:break

    next_arr = remove(start, cnt)
    arr = next_arr[:]

print(len(arr))
for ele in arr:
    print(ele)