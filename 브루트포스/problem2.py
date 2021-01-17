# 분해합
num = int(input())
result = 0
for i in range(0,num):
    array = list(str(i))
    array = [int(i) for i in array]
    if(sum(array)+i == num):
        result = i
        break
print(result)
