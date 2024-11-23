import sys
input = sys.stdin.readline 

n, l = map(int, input().split())
dots = [int(input()) for _ in range(n)]
dots.sort()
start, end = dots[0], dots[-1]

answer = 0
def separate_dots(standard):
    right_dots, left_dots = [], []

    for dot in dots:
        if dot < standard:
            right_dots.append(dot)
        elif dot > standard:
            left_dots.append(dot)
    return right_dots[::-1], left_dots

for i in range(start+1, end):
    # 오른쪽에 잇는 점
    right_dots, left_dots = separate_dots(i)
    # abs(i-right_dot) == abs(i - left_dot)
    flag = True
    min_len = min(len(left_dots), len(right_dots))
    for idx in range(min_len):
        if abs(i-right_dots[idx]) != abs(i-left_dots[idx]):
            flag = False
            break 
    if flag:
        # print(i, right_dots, left_dots)
        answer += 1
print(answer)
            
                

        
    