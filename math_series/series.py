def fibonacci(n):
    # if n in (0, 1):
    #     return n
    # return fibonacci(n - 1) + fibonacci(n - 2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    # return sum_series(n, 0, 1)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
    # return sum_series(n, 2, 1)


def sum_series(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b

    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


print(sum_series(5, 13, 6))
