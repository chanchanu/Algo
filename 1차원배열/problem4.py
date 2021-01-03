# 나머지가 다른 개수 구하기
array = []
for i in range(10):
    a = int(input())
    x = a%42
    array.append(x)
array = set(array)
print(len(array))