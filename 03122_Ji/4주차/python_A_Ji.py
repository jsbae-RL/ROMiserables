'''
내장 함수 문제
'''

# 1
print(f'1: {abs(-5)}')

# 2 전부 true
numbers = [True, True, False]
print(f'2: {all(numbers)}')         # 리스트에 숫자 0있으면 False,'':False?

# 3 
numbers = [0, 0, 1]
print(f'3: {any(numbers)}')

# 4
words = ["a", "b", "c"]
print(f'4: {list(enumerate(words))}')

# 5
numbers = [1, 2, 3, 4, 5]
print(f'5: {list(filter(lambda x:x%2==0,numbers))}')

# 6
numbers = [1, 2, 3]
print(f'6: {len(numbers)}')

# 7
numbers = [10, 20, 30]
print(f'7: {max(numbers)}')

# 8
numbers = [10, 20, 30]
print(f'8: {min(numbers)}')

# 9
numbers = [1, 2, 3]
print(f'9: {list(map(lambda x: x ** 2, numbers))}')

# 10
print(f'10: {pow(2,3)}')

# 11
print(f'11: {list(range(5))}')

# 12
numbers = [1, 2, 3]
print(f'12: {reversed(numbers)}')

# 13
print(f'13: {round(3.14159, 2)}')

# 14
numbers = [3, 1, 2]
print(f'14: {sorted(numbers)}')

# 15
numbers = [1, 2, 3]
print(f'15: {sum(numbers)}')

# 16
value = 42
print(f'16: {type(value)}')

# 17    ## zip 으로 묶어서 딕셔너리 만들 수 있음
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(f'17: {list(zip(list1,list2))}')

# 18
expression = "2 + 3 * 4"
print(f'18: {eval(expression)}')

# 19
print(f'19: {chr(97)}')

# 20
print(f'20: {ord('a')}')


'''
정규 표현식 문제
'''
print('-----정규 표현식 문제-----')
# 1
import re
text = "Contact us at info@example.com or support@domain.org"
p = re.compile('\w+@\w+[.]\w+')
s = p.findall(text)
print(f'1: {s}')

# 2
text = "apple banana cherry date"
pattern = r"^a"
p = re.compile('^a\w+')
s = p.findall(text)
print(f'2: {s}')

# 3
phone = "123-456-7890"
p = re.compile('\d{3}-\d{3}-\d{4}')
s = p.match(phone)
print(f'3: {bool(s)}')

# 4
text = "Order 123 items for $45.67"
p = re.compile('\d+')
s = p.findall(text)
print(f'4: {s}')

# 5
text = "This is a test sentence."
p = re.compile('\s')
s = len(p.findall(text)) + 1
print(f'5: {s}')

# 6
html = "<p>This is a paragraph.</p>"
p = re.compile('</?p>')
s = p.findall(html)
for char in s:
    html=html.replace(char, '')
print(f'6: {html}')

# 7
text = "Python is fun"
word = "fun"
p = re.compile(text)
s = p.search(text)
print(f'7: {bool(s)}')

# 8 sub (괄호 안에 있으면 인덱스로)
date = "2025-01-27"

# 9 lambda
text = "Hello World"

# 10
ip = "192.168.1.1"
p = re.compile('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
s = p.match(ip)
print(f'10: {bool(s)}')

# 11
text = "Visit https://example.com or http://test.org for info."
p = re.compile('https?://[a-zA-z0-9.-]+[.]\w+')
s = p.findall(text)
print(s)

# 12
text = "I love cats and dogs"
pattern = r"cats"
replacement = "pets"
result = re.sub(pattern, replacement,text)
print(f'12: {result}')

# 13
text = "This   is   a  test."
result=re.sub(' +',' ',text)
print(f'13: {result}')

# 14
path = "/user/home/test.txt"

# 15
text = "123abc!@#def456"
p = re.compile('[a-zA-Z]+')
s = p.findall(text)
print(f'15: {s}')

# 16
text = "running swimming jumping"
pattern = r"ing"
p = re.compile('\w+ing')
s = p.findall(text)
print(f'16: {s}')

# 17    ## sub
text = "this this is is a test test"


# 18
text = "Hello!@#$%^&*()"
p = re.compile('\w+')
s = p.match(text)
print(f'18: {s.group()}')

# 19
text = "cat bat mat"
length = 3
p = re.compile(r'\b\w{3}\b')
s = p.findall(text)
print(f'19: {s}')

# 20
filename = "document.pdf"
p = re.compile('\w+[.]')
s = p.match(filename).group()
filename = filename.replace(s,'')
print(f'20: {filename}')