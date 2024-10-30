n = int(input())
start, end = 1, 2
value = 1

answer = 0


while start <= n:
    if value == n:
        answer += 1
        value -= start 
        start += 1
    elif value > n:
        value -= start
        start += 1
    else:
        value += end 
        end += 1


print(answer)