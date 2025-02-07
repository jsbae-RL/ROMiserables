#01
print(abs(-5))

#02
numbers=[True,True,False]
print(all(numbers))

#03
numbers=[0,0,1]
print(any(numbers))

# #04
# words=["a","b","c"]
# answer=[]
# for index,value in enumerate(words):
#     # answer.append(index,value)
# print(answer)

#05
is_even=list(filter(lambda x: x%2==0,numbers))
print(is_even)

#06
numbers=[1,2,3]
print(len(numbers))

#07
numbers=[10,20,30]
print(max(numbers))

#08
numbers=[10,20,30]
print(min(numbers))

#09
numbers=[1,2,3]
squared=list(map(lambda x: x**2,numbers))
print(squared)

#10
numbers=[1,2,3]
squared=list(map(lambda x:pow(x,2),numbers))
print(squared)

#11
print(list(range(5)))


#12
numbers=[1,2,3]
print(list(reversed(numbers)))

#13
print(round(3.14159,2))

#14
numbers=[3,1,2]
print(sorted(numbers))

#15
numbers=[1,2,3]
print(sum(numbers))

#16
value=42
print(type(value))

#17
list1=[1,2,3]
list2=["a","b","c"]
print(dict(zip(list1,list2)))

#18
expression="2+3*4"
print(eval(expression))

#19
print(chr(97))

#20
print(ord('a'))



#01
text = "Contact us at info@example.com or support@domain.org"
