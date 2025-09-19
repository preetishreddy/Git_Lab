def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

def is_prime(n: int) -> bool :
    if n<2 :
        return False
    if n%2 == 0:
        return n==2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

#print(is_prime(13))