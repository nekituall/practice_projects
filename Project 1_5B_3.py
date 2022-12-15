

def double(x):
    """обычный квадрат аргумента"""
    return round(x*x, 2)

print(double(5.64))
print(double(5))
print(double(-5))


def recursion(x):
    """Рескурсивно квадрат"""
    if x == 0:
        return x
    else:
        return recursion(x-1) + 2*x -1

print(recursion(6))

