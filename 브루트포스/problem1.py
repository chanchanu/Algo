# 블랙잭 변형
a,b = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]
array = sorted(list(array))
sums = []
max = 0
for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            sum = array[i] + array[j] + array[k]
            sums.append(sum)
sums = sorted(set(sums))

for i in sums:
    if ((i >= max) & (i <= b)):
        max = i
print(max)