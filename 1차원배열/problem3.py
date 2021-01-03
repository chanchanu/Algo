# 세 수의 곱에 있는 숫자 개수 구하기
x = 1
for i in range(3):
    a = int(input())
    x = x * a
x = str(x)
for i in range(10):
    print(x.count(str(i)))