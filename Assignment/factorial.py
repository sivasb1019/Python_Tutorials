def fact(n):
    if n > 1:
        return n * fact(n-1)
    return n


print(fact(0))