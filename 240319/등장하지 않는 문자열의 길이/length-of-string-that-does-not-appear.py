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
        
        if repeat == 1: # 한번도 반복되지 않은 경우
            answer = length
        else: # 반복된 경우 
            repeat_cnt += 1

    if repeat_cnt == 0: # 한번도 반복되지 않은 문자열의 길이
        answer = length
        break


print(answer)