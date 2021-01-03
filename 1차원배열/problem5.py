# 시험 성적 변경
n = int(input()) # 시험 본 과목 개수
array = []
newarray = []
array = input().split()
array = [int(i) for i in array]
m = max(array)

for i in array:
    newarray.append(i/m*100)
print(sum(newarray)/len(newarray))