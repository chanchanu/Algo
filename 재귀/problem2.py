# 피보나치 
def fib(n):
    result = 0
    if(n == 0):
        result = 0
    elif(n == 1):
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

n = int(input())
print(fib(n))



