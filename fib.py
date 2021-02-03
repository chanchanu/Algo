import math
# O(n)인 반복문
def fib1(n):
    if n < 2 :
        return n
    a,b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a

# O(2^n)인 재귀
def fib2(n):
    if n < 2:
        return n
    return fib2(n-1)+fib2(n-2)
