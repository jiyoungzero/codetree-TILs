import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def under_k():
    return max(arr) - min(arr) <= k 

def plus2min():
    global arr
    min_val = min(arr) 
    for i in range(len(arr)):
        if arr[i] == min_val:
            arr[i] += 1 

def deep_copy(a):
    return [
        a[i][:]
        for i in range(len(a))
    ]

def rolling():
    global arr
    nxt_arr = []
    time = 1
    while True:
        if time == 1:
            nxt_arr.append(arr[:1])
            nxt_arr.append(arr[1:])
        else:
            for col in range(len(arr[0])):
                new_row = []
                for row in range(len(arr)-1, -1, -1):
                    new_row.append(arr[row][col])
                nxt_arr.append(new_row)
            nxt_arr.append(arr[-1][len(arr[0]):])
            
        if len(nxt_arr[-1]) < len(nxt_arr[-2]):break 
        arr = deep_copy(nxt_arr)
        time += 1
        nxt_arr = []



def pushing():
    global arr
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    tmp_arr = deep_copy(arr)
    max_len = len(tmp_arr[-1])
    for i in range(len(tmp_arr[:-1])):
        for j in range(max_len-len(tmp_arr[i])):
            tmp_arr[i].append(-1)

    for i in range(len(tmp_arr)):
        for j in range(max_len):
            if tmp_arr[i][j] == -1:continue
            for dir in range(4):
                ni, nj = i + dxs[dir], j + dys[dir]
                if ni < 0 or ni >= len(tmp_arr) or nj < 0 or nj >= max_len: continue
                if tmp_arr[ni][nj] == -1: continue
                d = abs(tmp_arr[i][j] - tmp_arr[ni][nj])//5
                if tmp_arr[i][j] > tmp_arr[ni][nj]:
                    arr[i][j] -= d 
                else:
                    arr[i][j] += d 
    # print()
    # for row in arr:
    #     print(*row)
    # print()
    nxt_arr = []
    for col in range(len(arr[0])):
        for row in range(len(arr)-1, -1, -1):
            nxt_arr.append((arr[row][col]))
    for ele in arr[-1][len(arr[0]):]:
        nxt_arr.append(ele)
    arr = nxt_arr[:]
    
def foldinhalf():
    global arr
    fold_arr = []
    h_idx = len(arr)//2
    fold_arr.append(arr[:h_idx][::-1])
    fold_arr.append(arr[h_idx:])

    nxt_fold_arr = []
    h_idx = len(fold_arr[0])//2
    for row in range(1, -1, -1):
        new_row = []
        for col in range(h_idx-1, -1, -1):
            new_row.append(fold_arr[row][col])
        nxt_fold_arr.append(new_row)

    for row in range(2):
        new_row = []
        for col in range(h_idx, len(fold_arr[0])):
            new_row.append(fold_arr[row][col])
        nxt_fold_arr.append(new_row)

    arr = deep_copy(nxt_fold_arr)
    return 



while not under_k():
    plus2min()
    rolling()
    pushing()
    foldinhalf()
    pushing()
    # print(arr)
    answer += 1
print(answer)