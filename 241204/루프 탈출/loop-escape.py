import sys
input = sys.stdin.readline 

n = int(input())
edges = [0]*(n+1)
for i in range(n):
    edges[i+1] = int(input())

def count_non_cyclic_nodes():
    # 0 : 미방문, 1 : 탐색 중, 2 : 완료
    visited = [0]*(n+1)
    non_cycle_cnt = 0

    def falling_loop(node):
        if visited[node] == 1: # 이미 방문한 곳 다시 방문 -> 순환 
            return True 
        if visited[node] == 2:
            return False 

        visited[node] = 1
        nxt_node = edges[node]
        if nxt_node != 0 and falling_loop(nxt_node):
            return True 
        
        visited[node] = 2
        return False
    
    for i in range(1, n+1):
        if visited[i] == 0:
            if not falling_loop(i):
                non_cycle_cnt += 1
    
    return non_cycle_cnt

print(count_non_cyclic_nodes())
        