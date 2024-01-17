import sys
input = sys.stdin.readline


given = list(input().rstrip())
n = len(given)
answer = int(1e9)

def run_length_encoding(arr):
    m = len(arr)
    result = 0
    idx, nxt_idx = 0, 1
    while 1: 
        cnt = 1
        if idx >= m:
            break       
        while nxt_idx < m and arr[nxt_idx] == arr[idx]:
            idx += 1
            cnt += 1
            nxt_idx = idx + 1
        result += (len(str(cnt))+ 1)
        idx = nxt_idx
        nxt_idx = idx + 1
        
    return result

for _ in range(n):
    answer = min(answer, run_length_encoding(given))
    given.insert(0, given.pop())

print(answer)