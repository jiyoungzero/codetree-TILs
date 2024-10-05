def no_carry_pairs(numbers):
    from itertools import combinations

    def is_valid_pair(a, b):
        while a > 0 and b > 0:
            if (a % 10) + (b % 10) >= 10:
                return False
            a //= 10
            b //= 10
        return True

    max_count = 0
    n = len(numbers)
    for r in range(1, n + 1):
        for combo in combinations(numbers, r):
            valid = True
            for i in range(r):
                for j in range(i + 1, r):
                    if not is_valid_pair(combo[i], combo[j]):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                max_count = max(max_count, r)

    return max_count

n = int(input())
numbers = [int(input()) for _ in range(n)]
print(no_carry_pairs(numbers))