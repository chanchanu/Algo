# 최대 구하고 index까지
array = []
for i in range(9):
    i = input()
    array.append(i)
array = [int(i) for i in array]
max = -1
for i in array:
    if max < i:
        max = i
print(max)
print(array.index(max)+1)
