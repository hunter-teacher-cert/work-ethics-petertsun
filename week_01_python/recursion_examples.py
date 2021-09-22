

def factorial(n):
    if n < 0:
        print('There is no factorial of a negative value')
        return
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1 # if n is 1 or 0 (zero), return a 1.

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



a = 6
print(f'{a}! = {factorial(a)}' )
print(f'fib({a}) = {fib(a)}')
    
