# 1
sum_num = lambda x,y: x+y
print(sum_num(3,5))

# 2
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2,numbers))
print(squared_numbers)

# 3
words = ["hello", "world"]
words_len = list(map(lambda x: len(x), words))
print(words_len)

# 4
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 5
from functools import reduce
numbers = [10, 20, 30, 40]
max_num = reduce(lambda x,y: x if x>y else y, numbers)
print(max_num)

# 7
words = ["banana", "apple", "cherry"]
print(sorted(words))

# 8
numbers = [5, 10, 15, 20]
fn = list(filter(lambda x: x>=10, numbers))
print(fn)

# 9
words = ["python", "lambda"]
cwords = list(map(lambda x: x.upper(), words))
print(cwords)

# 10
numbers = [4, 9, 16]
sr = list(map(lambda x: x ** 0.5, numbers))
print(sr)

# 11
words = ["hello", "world"]
w_words = list(filter(lambda x: 'w' in x, words))
print(w_words)

# 12
numbers = [1, 2, 3, 4]
multi_num = reduce(lambda x,y: x*y, numbers)
print(multi_num)

# 13
numbers = [1, 2, 3, 4, 5]
even = [x**2 for x in numbers if x%2 ==0]
print(even)

# 14
list1 = [1, 2, 3]
list2 = [4, 5, 6]
hap = list(map(lambda x,y: x+y, list1, list2))
print(hap)

# 15
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
people.sort(key=lambda x:x[1])
print(people)

# 16
plus_str = lambda str1,str2: str1+' '+str2
print(plus_str('hello','world'))

# 17
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x:x%2==0,numbers))
sum_even = sum(even)
print(sum_even)

# 18
words = ["apple", "banana"]
fw = list(map(lambda x: x[0], words))
print(fw)

# 19
numbers = [1, 2, 3]
print(list(map(lambda x:str(x),numbers)))

# 20
words = ["python", "is", "awesome"]
print(list(filter(lambda x: len(x)>=3, words)))