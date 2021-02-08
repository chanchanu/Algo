#  배열과 유사한것이 리스트이다.
# append(x) = A[len(A):] = [x]
people = ["김찬우", "최원혁"]
people.append("김민수")
# people[len(people):] = ["김민수"]
# people += ["김민수"]
print(people)   # ['김찬우', '최원혁', '김민수']

# extend(x) = A[len(A):] = c    or  A += c
p = ["김찬우", "최원혁"]
p.extend("김민수")
# p[len(p):] = "김민수"
# p += "김민수"
#
print(p)    # ['김찬우', '최원혁', '김', '민', '수']

# insert(i,x)
p = ["김찬우", "최원혁"]
p.insert(1, "김민수")
print(p)    # ['김찬우', '김민수', '최원혁']

# remove(x)     특정 항목을 삭제
p = ["김찬우", "최원혁"]
p.remove("김찬우")
print(p)    # ['최원혁"]

# pop(i)
p = ["김찬우", "최원혁"]
p.pop(0)

# del문     특정 인덱스를 삭제
p = ["a", "b", "c", "d"]
del p[0]
print(p)    # ["b", "c", "d",]
del p[0:1]
print(p)    # ["d"] 

# index(x)  인덱스를 반환
p = ["a", "b", "c"]
p.index("a")    # 0

# count(x)  x 개수 반환
p = ["a", "a", "v", "a"]
p.count("a")    # 3

# sort(key, reverse)    key는 함수를 넣어야한다.
p = ["b", "a", "c"]
p.sort()
print(p)    # ["a","b","c"]
p.sort(reverse=True)
print(p)    # ["c","b","a"]

# reverse()
p = ["a","b","c"]
p.reverse()
print(p)    # ["c","b","a"]
