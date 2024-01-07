import sys
input = sys.stdin.readline

BLANK = 0
n = int(input())
arr = [int(input()) for _ in range(n)]
commands = []
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    commands.append((s-1, e))

for command in commands:
    s, e = command
    tmp_arr = []
    for i in range(s, e):
        arr[i] = BLANK
    
    for ele in arr:
        if ele != BLANK:
            tmp_arr.append(ele)
    
    arr = tmp_arr[:]

print(len(arr))
for ele in arr:
    print(ele)