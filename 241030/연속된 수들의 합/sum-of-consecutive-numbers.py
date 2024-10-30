n = int(input())
arr = [ele for ele in range(1, n+1)]
start, end = 0,1
value = arr[start]

answer = 0
if value == n:
    answer += 1

while start <= end and end < n:
    if end + 1 < len(arr) and value < n:
        value += arr[end]
        end += 1
        
    else:
        value -= arr[start]
        start += 1
    
    if value == n:
        answer += 1
print(answer+1)