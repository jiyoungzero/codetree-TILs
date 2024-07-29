import sys
input= sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_subArr():
    i = 0
    for j in range(m):
        while i < n and A[i] != B[j]:
            i += 1
        if i >= n:
            return False
        i += 1
    return True


if is_subArr():
    print("Yes")
else:
    print("No")