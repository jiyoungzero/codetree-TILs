import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
answer = 0

def is_possible(a, b, c):
    # 1. 문자열로 변환하기
    # 2. 제일 긴 문자열 기준으로 0채우기
    # 3. 제일 긴 문자열만큼 반복문을 돌리며 각 자릿수 더하기
    # 4. 이 때 carry가 발생하면 false값으로 받음 
    str_a, str_b, str_c = str(a), str(b), str(c)
    max_len = max([len(str_a), len(str_b), len(str_c)])
    str_a = str_a.zfill(max_len)
    str_b = str_b.zfill(max_len)
    str_c = str_c.zfill(max_len)
    for i in range(max_len):
        if int(str_a[i])+int(str_b[i])+int(str_c[i]) >= 10:
            return False
    return True 

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if is_possible(nums[i], nums[j], nums[k]):
                answer = max(answer, nums[i]+nums[j]+nums[k])


print(answer if answer > 0 else -1)