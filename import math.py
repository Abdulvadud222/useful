import math
def square(x):
    return x ** 2
def t_func(func, *args):
    results = []
    for arg in args:
        results.append(func(arg)) 
    return results
print(t_func(square, 2, 3, 5))