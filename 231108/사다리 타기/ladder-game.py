n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))

lines.sort()

answer = m
path = []

# 사다리 타기 결과 
def is_same():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]

    for _, idx in lines: # 원래 결과
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    for _, idx in path: # 선택한 결과
        num2[idx], num2[idx+1] = num2[idx+1], num2[idx]

    for e1, e2 in zip(num1, num2):
        if e1 != e2:
            return False
    return True




# 선의 개수를 0개부터 시작해서 m개까지 늘려가면서 원래 결과와 같으면 return 
def backtracking(depth):
    global answer

    if depth >= m: # 오류 원인 : 선택 안하는 거까지 가야 하니까 depth을 끝까지 돌려줘야 함.!!!
        if is_same():
            answer = min(answer, len(path))
        return 

    path.append(lines[depth])
    backtracking(depth+1)
    path.pop()

    backtracking(depth+1)

if m > 1:
    backtracking(0)
    print(answer)
else:
    print(1)