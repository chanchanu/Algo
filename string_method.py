# 문자열 메소드
# leb min max

# join
l = ["w", "o", "r", "k"]
l = "".join(l)      # .join 앞에있는 방식대로 리스트를 join한다.
print(l)
l = "".join(reversed(l))    # reversed() 메소드 같이 사용 가능
print(l)

# ljust, rjust
l = "cksdn514"
l.ljust(10,'-')     # ljust(width, fillchar)
l.rjust(10,'-')     # rjust(width, fillchar)

# format
print("{0} {1}".format("안녕", "모현"))
print("이름: {who}  나이: {age}".format(who = "김찬우", age="25"))
print("이름: {who}  나이: {0}".format(12, who = "김찬우"))  # 0부터 시작
a = "gkgk"
b = "23"
print("이름: {who}  나이: {age}".format(who = a, age= b))   # 변수도 가능

# split
l = "김치 치즈 볶음밥"
l = l.split(" ")    # 띄어쓰기 단위로 split l.split() 해도 공백단위
print(l)
l = "12345"
l = l.split("")       # 문자단위 split
print(l)

# split 활용해서 스페이스 제거 함수
def erase_space_from_string(string):
    s1 = string.split(" ")
    s1 = "".join(s1)
    return s1

# strip

# upper lower
a = "asd"
b = "ASD"
print(a.upper())
print(b.lower())

# index, find (sub, start, end) 인데 주로 sub만 쓰는경우가 많다.
# 둘다 index를 반환하는데 차이는 못찾았을떄, index는 에러 find는 -1 반환
l = "i am chan woo kim"
print(l.index('w'))
print(l.find('a'))

# count (sub, start, end) 인데 주로 sub만 쓰는경우가 많다.
l = "ha ha ha 1"
print(l.count("ha"))

# replace (old, new, maxreplace)
l = "ha ha ha 1"
print(l.replace("ha", "ho",1))


