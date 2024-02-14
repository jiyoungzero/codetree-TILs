import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [0] + list(map(int, input().split()))
parent = [0]*(n+1)

finding_node = -1
answer = 0
for i in range(1, n+1):
    if nums[i] == k:
        finding_node = i

# 계층별 부모 노드 인덱스 설정
parent_node = 0
for i in range(2, n+1):
    if nums[i-1]+1 < nums[i]:
        parent_node += 1
    parent[i] = parent_node

# 부모의 노드 인덱스는 다르지만, 부모의 부모 번호가 같은 경우
for i in range(2, n+1):
    if parent[finding_node] != parent[i] and parent[parent[finding_node]] == parent[parent[i]]:
        answer += 1

print(answer)