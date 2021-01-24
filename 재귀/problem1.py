# 팩토리얼 
def fact(n):
    result = 0
    if (n==0 or n==1):
        return 1
    if(n>=0):
        result = n * fact(n-1)
    return result
n = int(input())
print(fact(n))