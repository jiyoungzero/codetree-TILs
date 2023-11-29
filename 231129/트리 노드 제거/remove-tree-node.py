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




# 삭제하고자 하는 본인노드 자식 + 그의 자식까지 지우기
# del tree[del_node]
del_lst = [del_node] # 삭제해야 할 노드들
delAll = False 

while not delAll:
    tmp = []
    delAll = True 
    for node in del_lst:
        if len(tree[node]) != 0:
            delAll = False
    if delAll:
        break
    
    while del_lst:
        node = del_lst.pop()
        tmp = tree[node]
        for t in tree:
            if node in t:
                t.remove(node)
        if tree[node] : 
            tree[node] = [] 
    del_lst = tmp


    

answer = 0
for t in tree:
    answer += (len(t))



print(answer)