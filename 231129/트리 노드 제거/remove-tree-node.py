import sys
input = sys.stdin.readline


n = int(input())
parent = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(n)]


# parent토대로 트리 만들어 보기 
for child, p in enumerate(parent):
    if p == -1:continue
    elif child == p:continue
    else:tree[p].append(child)




# 삭제하고자 하는 본인노드 자식 지우기
del tree[del_node]


answer = 0
# 삭제하고자 하는 본인노드 지우기
for t in tree:
    if del_node in t:
        answer += (len(t) - 1)
    elif len(t) > 0:
        answer += (len(t))
print(answer)