import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = -1



def all_plus(si, sj, ei, ej):
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if arr[i][j] <= 0:
                return False
    return True

for si in range(n):
    for sj in range(m):
        for ei in range(si, n):
            for ej in range(sj, m):
                if all_plus(si, sj, ei, ej):
                    answer = max(answer, (ei-si+1)*(ej-sj+1))
    
print(answer if answer > 0 else -1)