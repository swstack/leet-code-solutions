import time


memo_cache = {}


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_memoized(n):
    if n == 0 or n == 1:
        return 1

    cached = memo_cache.get(n, None)
    if cached:
        return cached

    memo_cache[n] = n * factorial(n - 1)
    return memo_cache[n]


def factorial_memoized_iterative(n):
    # Iterative implementation to avoid recursion-limit/stack-size issues

    result = 1
    for i in range(1, n + 1):
        if i == 0 or i == 1:
            continue

        # Memoization: hash table lookup faster than multiplication
        cached = memo_cache.get(i, None)
        if cached:
            result = cached
        else:
            result = result * i
            memo_cache[i] = result

    return result


assert factorial(5) == 120
assert factorial_memoized(5) == 120
assert factorial_memoized(5) == 120
assert factorial_memoized_iterative(5) == 120
assert factorial_memoized_iterative(5) == 120

# Test performance
memo_cache.clear()
pass_1_start = time.time()
factorial_memoized_iterative(1000)
print("First pass took: {} seconds".format(time.time() - pass_1_start))

pass_2_start = time.time()
factorial_memoized_iterative(1000)
print("Second pass took: {} seconds".format(time.time() - pass_2_start))


pass_3_start = time.time()
factorial_memoized_iterative(1000)
print("Third pass took: {} seconds, should be same or similar to pass 2.".format(time.time() - pass_3_start))
