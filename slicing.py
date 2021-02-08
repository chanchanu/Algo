x = list(range(10))  # is the list [0, 1, ..., 9]
zero = x[0]  # equals 0, lists are 0-indexed
one = x[1]  # equals 1
nine = x[-1]  # equals 9, 'Pythonic' for last element
eight = x[-2]  # equals 8, 'Pythonic' for next-to-last element
x[0] = -1  # now x is [-1, 1, 2, 3, ..., 9]
first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]

#[:] 처음부터 끝까지
#[start:] start오프셋부터 끝까지
#[:end] 처음부터 end-1 오프셋까지 
#[start : end] start오프셋부터 end-1 오프셋까지
#[start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출

print(x[::2])   # [-1, 2, 4, 6, 8]  처음부터 끝까지 2씩 건너뛰며
print(x[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]   처음부터 끝까지 거꾸로
1 in [1, 2, 3]  # True
0 in [1, 2, 3]  # False
x = [1, 2, 3]
y = x + [4, 5, 6]  # y is [1, 2, 3, 4, 5, 6]; x is unchanged

document = ['I', 'am', 'a', 'boy', 'I', 'love', 'you']
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
