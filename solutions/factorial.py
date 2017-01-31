def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_memoized(n):
    pass


assert factorial(5) == 120
