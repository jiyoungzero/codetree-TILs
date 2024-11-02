n, m = map(int, input().split())

def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1) * num

print(int(factorial(n)/factorial(m)*factorial(n-m)))