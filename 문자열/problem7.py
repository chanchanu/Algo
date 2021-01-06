# reverse 문제
array = (input().split())
a = array[0]
b = array[1]
a = a[::-1]
b = b[::-1]
if (a>b):
    print(a)
else:
    print(b)