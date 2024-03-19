import sys
input = sys.stdin.readline 

n = int(input())
string = input().rstrip()
answer = 0
    
for length in range(1, n):
    repeat = 1
    repeat_cnt = 0
 
    for start in range(n):
        target = string[start:start+length]
        for i in range(start+1, n):
            # print(target, string[i:i+length], i, length)
            if target == string[i:i+length]:
                repeat += 1
        
        if repeat == 2:
            answer = length
        else:
            repeat_cnt += 1
        # print()

    if repeat_cnt == 0:
        answer = length
        break


print(answer+1)