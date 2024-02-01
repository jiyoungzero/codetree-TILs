from collections import deque
import sys
import enum

OPERATOR_NUM = 4
INT_MAX = sys.maxsize

class OPERATOR(enum.Enum):
    SUBTRACT = 0
    ADD = 1
    DIV2 = 2
    DIV3 = 3
    
n = int(input())
ans = INT_MAX

q = deque()
visited = [False for _ in range(2 * n)]

# step[i] : 정점 n에서 시작하여 정점 i 지점에 도달하기 위한 
# 최단거리를 기록합니다.
step = [0 for _ in range(2 * n)]

# num이라는 값에 해당 operator를 사용할 수 있는지를 판단합니다.
# 2로 나누거나 3으로 나누려는 경우 num이 해당 값으로 나누어 떨어질 때에만
# 해당 연산을 사용 가능합니다.
def possible(num, op):
    if op == OPERATOR.SUBTRACT.value or op == OPERATOR.ADD.value:
        return True
    elif op == OPERATOR.DIV2.value:
        return num % 2 == 0
    else:
        return num % 3 == 0

    
# num에 op 연산을 수행했을 때의 결과를 반환합니다.
def calculate(num, op):
    if op == OPERATOR.SUBTRACT.value:
        return num - 1
    elif op == OPERATOR.ADD.value:
        return num + 1
    elif op == OPERATOR.DIV2.value:
        return num // 2
    else:
        return num // 3
        
# 1에서 2n - 1 사이의 숫자만 이용해도 올바른 답을 구할 수 있으므로 
# 그 범위 안에 들어오는 숫자인지를 확인합니다.
def in_range(num):
    return 1 <= num and num <= 2 * n - 1


# 1에서 2n - 1 사이의 숫자이면서 아직 방문한 적이 없다면 가야만 합니다. 
def can_go(num):
    return in_range(num) and not visited[num]

# queue에 새로운 위치를 추가하고 방문 여부를 표시해줍니다.
# 시작점으로 부터의 최단거리 값도 갱신해줍니다.
def push(num, new_step):
    q.append(num)
    visited[num] = True
    step[num] = new_step
    
# BFS를 통해 최소 연산 횟수를 구합니다.
def find_min():
    global ans
    
    # queue에 남은 것이 없을때까지 반복합니다.
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        curr_num = q.popleft()
        
        # queue에서 뺀 원소의 위치를 기준으로 4가지 연산들을 적용해봅니다.
        for i in range(OPERATOR_NUM):
            # 연산을 적용할 수 없는 경우라면 패스합니다.
            if not possible(curr_num, i):
                continue
            
            new_num = calculate(curr_num, i)
            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면 새로 queue에 넣어줍니다.
            if can_go(new_num):
                # 최단 거리는 이전 최단거리에 1이 증가하게 됩니다. 
                push(new_num, step[curr_num] + 1)
        
        # 1번 정점까지 가는 데 필요한 최소 연산 횟수를 답으로 기록합니다.
        ans = step[1]

# BFS를 통해 최소 연산 횟수를 구합니다.
push(n, 0)
find_min()            
print(ans)