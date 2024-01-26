import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = -int(1e9)
cases = []

for si in range(n):
    for sj in range(m):
        for ei in range(si, n):
            for ej in range(sj, m):
                cases.append((si, sj, ei, ej))

def get_sum(idx):
    result = 0
    si, sj, ei, ej = cases[idx]
    for x in range(si, ei+1):
        for y in range(sj, ej+1):
            result += arr[x][y]
    return result

def duplicate(a, b):
    f_si, f_sj, f_ei, f_ej = cases[a]
    s_si, s_sj, s_ei, s_ej = cases[b]
    if f_ej >= s_sj:
        return True
    return False


for i in range(len(cases)):
    for j in range(i+1, len(cases)):
        if duplicate(i, j):
            continue
        else:
            first = get_sum(i)
            second = get_sum(j)
            answer = max(answer, first+second)
print(answer)