import math

# 일반적 prime_number 찾기
def prime(n):
    n = abs(n)
    if n < 4:
        return True
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

# sqrt를 이용한 조금 더 빠른 방법
def prime2(n):
    n = abs(n)
    if n < 4:
        return True
    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True

