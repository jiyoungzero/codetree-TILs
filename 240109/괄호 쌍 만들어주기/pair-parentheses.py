import sys
input = sys.stdin.readline

arr = input()
n = len(arr)
open_, close = 0, 0

for i in range(n-1):
    if arr[i:i+2] == "((":
        open_ += 1
    elif arr[i:i+2] == '))':
        close += 1
print(close*open_)