# 풀이 1
arr1, arr2 = [[1,2],[2,3]], [[3,4],[5,6]]

total_array = []
for i in range(len(arr1)):
    sub = []
    for j in range(len(arr1[i])):
        sub.append(arr1[i][j]+arr2[i][j])
    total_array.append(sub)

print(total_array)

# 풀이 2
arr1, arr2 = [[1,2],[2,3]], [[3,4],[5,6]]
fadd = lambda x, y : x+y 

total_array = []
for i in range(len(arr1)):
    sub = []
    for j in range(len(arr1[i])):
        sub.append(fadd(arr1[i][j],arr2[i][j]))
    total_array.append(sub)

print(list(total_array))


# 풀이 3
arr1, arr2 = [[1,2],[2,3]], [[3,4],[5,6]]
total_array = list(map(lambda a, b: list(map(lambda x, y: x + y, a, b)), arr1, arr2))
print(total_array)