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
    if arr[0] + 2 == arr[1]:
        answer += 1
        break
    arr[2] = arr[0] + 2
    answer +=1

    

print(answer)