n=100
def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x
