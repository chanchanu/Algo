# 가장 많은 문자 출력 (여러개일때 ? 출력)
array = input()
array = array.upper()
array = list(array)
mid=[]
m = 0
result = 0
for i in range(65,91):
    mid.append(array.count(chr(i)))
    if(m < array.count(chr(i))):
        m = array.count(chr(i))
        result = chr(i)
if(mid.count(max(mid))>1):
    result = '?'
print(result)